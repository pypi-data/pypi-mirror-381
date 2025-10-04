#!/usr/bin/env python
# [[file:../Empirics/regression.org::*Outer product of two series][Outer product of two series:1]]
# Tangled on Mon Aug 11 07:17:24 2025
import numpy as np
import pandas as pd

def outer(a,b):
    """
    Outer product of two series.
    """

    if type(a) is pd.DataFrame:
        a = a.squeeze()

    if type(b) is pd.DataFrame:
        b = b.squeeze()

    a = pd.Series(a)
    b = pd.Series(b)

    x = np.outer(a,b)

    try:
        x = pd.DataFrame(x,index=a.index,columns=b.index)
    except AttributeError:
        x = pd.DataFrame(x)

    return x
# Outer product of two series:1 ends here

# [[file:../Empirics/regression.org::*Inner product][Inner product:1]]
# Tangled on Mon Aug 11 07:17:24 2025
def to_series(df):
    """
    Stack a dataframe to make a series.
    """
    try:
        df.columns.names = [n if n is not None else "_%d" % i for i,n in enumerate(df.columns.names)]
    except AttributeError: # Already a series?
        return pd.Series(df)

    for n in df.columns.names:
        df = df.stack(n)

    return df

def inner(a,b,idxout,colsout,fill_value=None,method='sum'):
    """
    Compute inner product of sorts, summing over indices of products which don't appear in idxout or colsout.
    """

    a = to_series(a)
    b = to_series(b)

    if fill_value is not None:
        a = a.astype(pd.SparseDtype(fill_value=fill_value))
        b = b.astype(pd.SparseDtype(fill_value=fill_value))

    idxint = list(set(a.index.names).intersection(b.index.names))
    aonly = list(set(a.index.names).difference(idxint))
    bonly = list(set(b.index.names).difference(idxint))

    if fill_value is None: # Non-sparse
        a = a.replace(0.,np.nan).dropna()
        b = b.replace(0.,np.nan).dropna()

    c = pd.merge(a.reset_index(aonly),b.reset_index(bonly),on=idxint)
    c = c.reset_index().set_index(idxint + aonly + bonly)

    sumover = list(set(aonly+bonly+idxint).difference(idxout+colsout))
    keep = list(set(aonly+bonly+idxint).difference(sumover))

    if fill_value is not None:
        foo = c.sparse.to_coo().tocsr()

        foo = foo[:,0].multiply(foo[:,1])
        foo = pd.DataFrame.sparse.from_spmatrix(foo,index=c.index)
    else:
        foo = c.iloc[:,0]*c.iloc[:,1]

    if method=='sum':
        p = foo.groupby(keep).sum()
    elif method=='mean':
        p = foo.groupby(keep).mean()
    else:
        raise ValueError("No method %s." % method)

    p = p.unstack(colsout)

    if len(idxout)>1:
        p = p.reorder_levels(idxout)

    p = p.sort_index()

    if len(colsout):
        p = p.sort_index(axis=1)

    return p
# Inner product:1 ends here

# [[file:../Empirics/regression.org::*Inter-quartile range][Inter-quartile range:1]]
# Tangled on Mon Aug 11 07:17:24 2025
def iqr(x,std=False):
    y = np.diff(x.quantile([0.25,0.75]))[0]

    # Ratio between std deviation and iqr for normal distribution
    if std: y = y*1.3489795

    return y
# Inter-quartile range:1 ends here

# [[file:../Empirics/regression.org::code:Mp][code:Mp]]
# Tangled on Mon Aug 11 07:17:24 2025
import pandas as pd
import numpy as np
from warnings import warn

def Mp(X):
    """
    Construct X-E(X|p) = (I-S(S'S)^{-1}S')X.

    Drop any categorical variables where taking means isn't sensible.
    """
    if len(X.shape) > 1:
        X = X.loc[:,X.dtypes != 'category']
    else:
        if X.dtype == 'category': warn('Taking mean of categorical variable.')

    use = list(set(['t','m','j']).intersection(X.index.names))

    if len(use):
        return X - X.groupby(use).transform("mean")
    else:
        return X - X.mean()
# code:Mp ends here

# [[file:../Empirics/regression.org::code:Mpi][code:Mpi]]
# Tangled on Mon Aug 11 07:17:24 2025

def Mpi(X):
    """
    Construct X-E(X|pi).

    Drop any categorical variables where taking means isn't sensible.
    """
    if len(X.shape) > 1:
        X = X.loc[:,X.dtypes != 'category']
    else:
        if X.dtype == 'category': warn('Taking mean of categorical variable.')

    return X - X.groupby(['t','m']).transform("mean")
# code:Mpi ends here

# [[file:../Empirics/regression.org::code:kmeans][code:kmeans]]
# Tangled on Mon Aug 11 07:17:24 2025
from sklearn.model_selection import GroupKFold
from .df_utils import use_indices, drop_missing
from sklearn.cluster import KMeans

def kmean_controls(n_clusters,Y,d,shuffles=0,classifiers=None,verbose=False):
    """
    Use kmeans to classify households into clusters; Construct MdY
    """
    n_clusters = int(n_clusters)
    d = d.copy()

    km = KMeans(n_clusters=n_clusters,init='k-means++',n_init=10*int(np.ceil(np.sqrt(n_clusters))))
    tau = km.fit_predict(d)

    if classifiers is not None:
        c = classifiers.values.T.tolist()
        d['tau'] = list(zip(*c,tau))
    else:
        d['tau'] = tau

    d['tau'] = d['tau'].astype('category')

    return d['tau']
# code:kmeans ends here

# [[file:../Empirics/regression.org::*\(\mathcal{M}_d\) operator][\(\mathcal{M}_d\) operator:1]]
# Tangled on Mon Aug 11 07:17:24 2025
def Md_generator(X,d,method='categorical',expected=False,Mpd=False):
    """
    Md operator, for either categorical or linear expectations.

    If expected is True, return E(X|d) rather than X-E(X|d).
    """
    if method=='categorical':
        try:
            groups = d.columns.tolist()
        except AttributeError: # d is a series?
            if d.name is None: d.name = 'tau'
            groups = [d.name]
        if 'j' in X.index.names: groups += 'j'
        if Mpd: groups += ['t','m']
        groups = list(set(groups)) # Eliminate dupes

        Xg = pd.DataFrame({'X':X}).join(d,how='left').groupby(groups)

        gamma_d = Xg.transform("mean").squeeze()
        gamma_d.name = 'gamma_d'

        if expected: return gamma_d,None

        MdX = X - gamma_d

    elif method=='linear':
        d = pd.DataFrame(d)

        # Add constant column if one doesn't exist in d
        d = d - d.mean()
        d['Constant'] = 1  # Constant just picks up means of X

        if 'j' in X.index.names:
            Xj = X.groupby('j',observed=True)
            if 'j' in d.index.names: dj = d.groupby('j')
            if expected: # Really return gamma_d,gamma
                EdX = {}
                Gamma = {}
                for j,y in Xj:
                    if 'j' in d.index.names:
                        x = dj.get_group(j).droplevel('j')
                    else:
                        x = d
                    EdX[j],Gamma[j] = Md_generator(y.droplevel('j'),x,method='linear',expected=True,Mpd=Mpd)
                EdX = pd.DataFrame(EdX)
                EdX.columns.name = 'j'
                Gamma = pd.DataFrame(Gamma).T
                Gamma.index.name = 'j'

                try:
                    EdX = EdX.stack()
                except AttributeError:
                    pass

                EdX = EdX.reorder_levels(['i','t','m','j']).sort_index()

                return EdX,Gamma
            else:
                MdX = {}
                for j,y in Xj:
                    if 'j' in d.index.names:
                        x = dj.get_group(j).droplevel('j')
                    else:
                        x = d
                    MdX[j] = Md_generator(y.droplevel('j'),x,
                                          method='linear',expected=False,Mpd=Mpd)
                MdX = pd.DataFrame(MdX)
                MdX.columns.name = 'j'

                try:
                    MdX = MdX.stack()
                except AttributeError:
                    pass

                MdX = MdX.reorder_levels(['i','t','m','j']).sort_index()

                return MdX
        else:
            y,x = drop_missing([X,d])

            if Mpd:
                y = y - y.groupby(['t','m']).transform('mean')
                x = x - x.groupby(['t','m']).transform('mean')

            gamma = np.linalg.lstsq(x,y,rcond=None)[0]

            gamma = pd.Series(gamma.squeeze(),index=x.columns)

            if expected:
                # NB: d, not x? Yes, because we can predict even missing values
                # this way.
                gamma_d = (d@gamma).squeeze()
                gamma_d.name = 'gamma_d'

                return gamma_d,gamma
            else:
                gamma_d = (x@gamma).squeeze()
                gamma_d.name = 'gamma_d'

            MdX = pd.Series(y.squeeze() - gamma_d,index=y.index)

    elif method=='mixed': # Some columns of d are categorical, others not
        if expected: raise NotImplementedError
        # Identify categorical columns
        cats = d.select_dtypes(['category']).columns
        xcols = d.columns.difference(cats)

        Z = X.join(d,how='outer')
        ycols = Z.columns.difference(xcols.union(cats))

        # Difference out means for each category
        if len(cats):
            Z = Z - Z.groupby(cats).transform("mean")
        else:
            Z = Z - Z.mean()

        y = Z[ycols]
        x = Z[xcols]

        MdX = Md_generator(y,x,method='linear') # Regress demeaned vars.

    else: raise ValueError("No method %s." % method)

    return MdX

def Ed(X,d,method='categorical'):
    return Md_generator(X,d,method=method,expected=True,Mpd=False)

def Epd(X,d,method='categorical'):
    return Md_generator(X,d,method=method,expected=True,Mpd=True)
# \(\mathcal{M}_d\) operator:1 ends here

# [[file:../Empirics/regression.org::*\(\mathcal{M}_{(p,d)}\) operator][\(\mathcal{M}_{(p,d)}\) operator:1]]
# Tangled on Mon Aug 11 07:17:24 2025
def Mpd_generator(X,tau,method='categorical',Mpd=False):
    """
    Md operator, for either categorical or linear expectations.

    If Mpd is True, operator is Mpd (i.e. condition on d & p jointly).
    """

    if method=='categorical': # assuming conditioning is on groups tau
        groups = ['tau']
        if 'j' in X.index.names: groups += 'j'
        if Mpd: groups += ['t','m']
        Xg = pd.DataFrame({'X':X}).join(tau,how='left').groupby(groups)

        MdX = X - Xg.transform("mean").squeeze()
    elif method=='linear':
        try:
            taucols = tau.columns
            X = pd.DataFrame(X).join(tau,how='outer')
        except AttributeError:  # tau a Series
            taucols = tau

        if 'j' in X.index.names:
            MdX = X.groupby('j').apply(lambda y,x=taucols: Md_generator(y.droplevel('j'),x,method='linear',Mpd=Mpd)).T
            try:
                MdX = MdX.stack()
            except AttributeError:
                pass

            MdX = MdX.reorder_levels(['i','t','m','j']).sort_index()
        else:
            # Difference out kmeans if tau provided
            ycols = X.columns.difference(taucols)
            xcols = taucols
            group = []
            if 'tau' in tau: # kmeans categories provided
                xcols = taucols.drop('tau')
                group += 'tau'
            if Mpd: group += ['t','m']

            if len(group):
                X = X - X.groupby(group).transform("mean")
            else:
                X = X - X.mean()

            y = X[ycols]
            x = X[xcols]
            y,x = drop_missing([y,x])
            x['Constant'] = 1
            b = np.linalg.lstsq(x,y,rcond=None)[0]
            MdX = pd.Series(y.squeeze() - (x@b).squeeze(),index=y.index)
    else: raise ValueError("No method %s." % method)

    return MdX
# \(\mathcal{M}_{(p,d)}\) operator:1 ends here

# [[file:../Empirics/regression.org::*Compute $\MpMdy$][Compute $\MpMdy$:1]]
# Tangled on Mon Aug 11 07:17:24 2025
def estimate_MpMdy(y,d,K=None,Mpd=False):

    if K is not None:
        d  = kmean_controls(K,Mp(y),Mp(d),classifiers=d.loc[:,d.dtypes == 'category'])
        method = 'categorical'
    else:
        method = 'linear'

        # Change categorical vars to numeric
        cats = d.select_dtypes(['category']).columns
        if len(cats):
            d[cats] = d[cats].apply(lambda x: x.cat.codes)

    Md = lambda x: Md_generator(x,d,method=method,Mpd=False)
    if Mpd:
        MpMd = lambda x: Md_generator(x,d,method=method,Mpd=True)
    else:
        MpMd = lambda x: Mp(Md(x))

    MpMdy = MpMd(y)

    assert MpMdy.index.names == ['i','t','m','j']

    if not np.all(np.abs(MpMdy.groupby(['j','t','m']).mean()) < 1e-6):
        warn('MpMdy means greater than 1e-6')

    return MpMdy,Md,MpMd,d
# Compute $\MpMdy$:1 ends here

# [[file:../Empirics/regression.org::code:beta_from_MdMpy][code:beta_from_MdMpy]]
# Tangled on Mon Aug 11 07:17:24 2025
from .estimation import svd_missing
import numpy as np

def estimate_beta(MpMdy,
                  heteroskedastic=False,
                  cov = lambda X : pd.DataFrame.cov(X,ddof=0),
                  return_se=False,bootstrap_tol=None,verbose=False):

    if verbose:
        print("estimate_beta")

    try:
        MpMdY = MpMdy.unstack('j')
    except KeyError:
        MpMdY = MpMdy

    C = cov(MpMdY)

    if np.any(np.isnan(C)):
        raise ValueError(f"Can't compute covariance matrix; too few {C.count().idxmin()}.")

    # Estimate beta
    u,s,vt = svd_missing(C,max_rank=1,heteroskedastic=heteroskedastic)

    if np.sign(u).mean()<0: # Fix sign of u.
        u = -u

    b = pd.DataFrame(u*s,index=MpMdY.columns,columns=['beta'])

    if return_se and bootstrap_tol:
        if bootstrap_tol is None:
            raise ValueError("Not implemented. Specify bootstrap_tol>0.")
            V = (((e-e.mean())**2).mul(v**2,axis=0)).mean() # See p. 150 of Bai (2003)
            seb = np.sqrt(V)
        else:
            its = 0
            B = None
            seb=0
            while its < 30 or np.linalg.norm(seb-last) > bootstrap_tol:
                last = seb
                okay = False
                while not okay:
                    try:
                        _b = estimate_beta(MpMdY.groupby(['t','m']).sample(frac=1,replace=True))[0]
                        B = pd.concat([B,_b.squeeze()],axis=1)
                        okay = True
                    except ValueError as msg:
                        print(msg)
                if its >= 29:
                    seb = B.apply(lambda x:iqr(x,std=True),axis=1)
                    if verbose: print(f"On iteration {its} standard error is {seb}.")
                its += 1
            V = B.T.cov()
    else:
        seb = None

    if return_se:
        return b,seb,V
    else:
        return b,None,None
# code:beta_from_MdMpy ends here

# [[file:../Empirics/regression.org::*Estimate Lagrange Multipliers][Estimate Lagrange Multipliers:1]]
# Tangled on Mon Aug 11 07:17:24 2025
def estimate_stderrs(y,scale):

    cols = y.groupby(['i','t','m']).mean().index

    TM = [(np.nan,t,m) for t in y.index.levels[y.index.names.index('t')] for m in y.index.levels[y.index.names.index('m')]]

    with warnings.catch_warnings():
        warnings.simplefilter('error')
            # X0inv = sparse.linalg.inv(X0)  # Too expensive!
        # se = np.sqrt(sparse.csr_matrix.diagonal(X0inv))

        # Use partioned matrix inverse to get just se of b
        BB = BB*(scale**2)
        # Note that BB is diagonal
        R = R.sparse.to_coo()
        n = B.shape[1]
        m = R.shape[0]
        Ainv = sparse.spdiags(1/BB.diagonal(),0,n,n)
        V22 = sparse.spdiags(1/(R@Ainv@R.T).diagonal(),0,m,m)
        V11 = Ainv - Ainv@R.T@V22@R@Ainv

        se = np.sqrt(V11.diagonal())

        if 'j' in Mpw.index.names:
            Mpw = Mpw[MpMdy.index]

        e1 = (MpMdy - B@Mpw)
        sigma2 = e1.var(ddof=0)

        mults_se = np.sqrt(V22.diagonal())*sigma2

        seb = pd.Series(se[:len(b)]*sigma2,index=b.index)
        mults_se = pd.Series(mults_se,
                            index=pd.MultiIndex.from_tuples([tm[1:] for tm in TM],
                                                            names=['t','m']),
                            name='mults_se')


    return seb, mults_se, e1
# Estimate Lagrange Multipliers:1 ends here

# [[file:../Empirics/regression.org::code:Ar_w][code:Ar_w]]
# Tangled on Mon Aug 11 07:17:24 2025
from scipy import sparse
from timeit import default_timer as timer

def estimate_w(y,beta,verbose=False):
    """
    Estimate regression $Mpi(Y - widehat{gamma(d)})  =  A(r) + hat{beta}w + e$.
    """
    try:
        y0 = y.stack()
    except AttributeError:
        y0 = y

    assert np.allclose(y0.groupby(['t','m']).mean(),0), "Pass Mpi(Y - gamma_d) to estimate_w."

    J = len(beta)

    beta = pd.DataFrame(beta)

    tm = [(t,m) for t in y0.index.levels[1] for m in y0.index.levels[2]]

    if len(y0.shape)==1 and y0.name is None: y0.name = 'y0'

    N = y0.index.levels[0]

    A = sparse.kron(sparse.kron(np.ones((len(N),1)),sparse.eye(len(tm))),np.ones((J,1)),format='csr')

    index = pd.MultiIndex.from_tuples([(i,t,m,j) for i in N for t,m in tm for j in beta.index.tolist()])

    A = pd.DataFrame.sparse.from_spmatrix(A,index=index)
    A.columns = pd.MultiIndex.from_tuples([(t,m) for t,m in tm])
    A.index.names = ['i','t','m','j']
    A.columns.names = ['t','m']

    cols = y0.groupby(['i','t','m']).mean().index

    index = pd.MultiIndex.from_tuples([(i[0],i[1],i[2],j) for i in cols.tolist() for j in beta.index.tolist()])

    B = sparse.kron(sparse.eye(len(cols)),beta,format='csr')
    B = pd.DataFrame.sparse.from_spmatrix(B,index=index,columns=cols)
    B.index.names = ['i','t','m','j']

    A = A.reindex(y0.index,axis=0)
    # This is very slow.
    B = B.loc[y0.index,:]

    X0 = pd.concat([A,B],axis=1)
    cols = X0.columns

    X0 = X0.sparse.to_coo()

    #start = timer()
    rslt = sparse.linalg.lsqr(X0,y0,atol=1e-16,btol=1e-16,show=verbose)
    #end = timer()
    #print("Time for lsqr %g" % (end-start,))
    b = pd.Series(rslt[0],index=cols)

    e = y0 - X0@b

    eg = e.groupby(['t','m','j'])

    Ar = eg.mean()
    Ar.name = 'Ar'

    # Missing data means that Ar.groupby(['t','m']).mean() may not be exactly zero; recenter.
    #Ar_bar = Ar.groupby(['t','m']).mean()
    #Ar = Ar - Ar_bar

    Ar_se = eg.std()/np.sqrt(eg.count())

    e3 = e - eg.transform("mean")

    what = pd.Series(b[len(A.columns):(len(A.columns)+len(B.columns))],index=B.columns)

    return what,Ar,Ar_se,e3
# code:Ar_w ends here

# [[file:../Empirics/regression.org::code:wvar][code:wvar]]
# Tangled on Mon Aug 11 07:17:24 2025
def w_var(e,beta):

    if len(e.shape)==1:
        e = e.unstack('j')

    sigma2=(beta@beta) # Should be principal eigenvalue of MdMpY

    v = (e.multiply(beta,axis=1)**2).mean(axis=1)/sigma2

    return v
# code:wvar ends here

# [[file:../Empirics/regression.org::code:pi][code:pi]]
# Tangled on Mon Aug 11 07:17:24 2025
def estimate_pi(y,b,w,Ar,gamma_d,verbose=False):

    try:
        y0 = y.stack()
    except AttributeError:
        y0 = y.copy()

    wb = outer(w,b).stack()

    e = y0 - Ar - wb - gamma_d

    e = e.dropna()

    pi_g = e.groupby(['t','m'])

    pi = pi_g.mean()
    pi.name = 'pi'

    pi_se = pi_g.std()/np.sqrt(pi_g.count())

    assert np.all(pi_se>0), "Non-positive estimates of pi_se?!"

    e4 = e - pi
    e4 = e4.reorder_levels(['i','t','m','j']).sort_index()

    return pi, pi_se, e4
# code:pi ends here

# [[file:../Empirics/regression.org::code:predict][code:predict]]
# Tangled on Mon Aug 11 07:17:24 2025
def predict_y(pi,Ar,gamma_d,beta,wr):
    bwr = outer(wr,beta).stack()

    yhat = pi + Ar + gamma_d + bwr

    return yhat.reorder_levels(['i','t','m','j']).sort_index()
# code:predict ends here

# [[file:../Empirics/regression.org::code:data_preparation][code:data_preparation]]
# Tangled on Mon Aug 11 07:17:24 2025
from .df_utils import broadcast_binary_op
from .estimation import drop_columns_wo_covariance
import matplotlib.pyplot as plt
from types import SimpleNamespace
from scipy.optimize import minimize_scalar

def prepare_data(y,d,min_obs=30,min_prop_items=0.1,alltm=False):
    assert y.index.names == ['i','t','m','j'], "Fix index names."

    # Deal with repeated observations
    y = np.log(np.exp(y).groupby(y.index.names).sum())

    y_in = y.copy()

    Y = y.unstack('j')

    if alltm:
        alltm = Y.groupby(['t','m']).count().replace(0,np.nan).dropna(axis=1).columns.tolist()
        Y = Y[alltm]
    else:
        Y.loc[:,Y.count()>min_obs] # Guaranteed to drop in drop_covariance

    # Drop household observations with fewer items than
    # min_prop_items*number of items
    items = Y.count(axis=1)
    Y = Y[items>(min_prop_items*Y.shape[1])]

    y = Y.stack('j').dropna()


    # Make d a dataframe, with columns k
    if 'k' in d.index.names:
        d = d.unstack('k')

    assert d.index.names==['i','t','m'], "Check names of index for d."
    for l in range(3):
        assert d.index.levels[l].dtype == y.index.levels[l].dtype, f"Mis-matched types for index of d & y in level {y.index.names[l]}."

    # Match up rows of d with y
    YD = pd.DataFrame({'y':y}).join(d,how='left')

    YD = YD.dropna()

    assert YD.shape[0]>0, "Join of y & d is empty."

    y = YD['y']  # Drops expenditures that lack corresponding d

    # Drop goods from y if not enough observations to calculate
    # covariance matrix
    Y = drop_columns_wo_covariance(y.unstack('j'),min_obs=min_obs)

    y = Y.stack('j').dropna()

    Ds =[]
    # If no variation in d across j, collapse
    numg = YD.iloc[:,1:].select_dtypes(exclude='category').groupby(['i','t','m'])
    if numg.count().shape[1]:  # There are some non-categorical ds
        if numg.std().mean().max()<1e-12:
            Ds.append(numg.head(1).droplevel('j')) # And vice versa

    catg = YD.iloc[:,1:].select_dtypes(include='category').groupby(['i','t','m'])
    if catg.count().shape[1]: # There are some categorical ds
        Ds.append(catg.head(1).droplevel('j')) # And vice versa

    d = pd.concat(Ds,axis=1)
    assert d.index.names == ['i','t','m']
    d.columns.name='k'

    if y_in.shape==y.shape:
        return y,d
    else:
        # Repeat this, because if we drop some goods because not alltm,
        # then that may drop some households below min_prop_item threshold
        # and vice versa.
        return prepare_data(y,d,min_obs=min_obs,min_prop_items=min_prop_items,alltm=alltm)

def find_optimal_K(y,d,shuffles=30,verbose=False):
    nstar = int(minimize_scalar(lambda k: -kmean_controls(k,Mp(y),Mp(d),
                                                          shuffles=30,
                                                          classifiers=d.loc[:,d.dtypes == 'category'],
                                                          verbose=verbose)[0],
                                    bracket=[1,20]).x)
    return nstar
# code:data_preparation ends here

# [[file:../Empirics/regression.org::*Construct Missing "correction"][Construct Missing "correction":1]]
# Tangled on Mon Aug 11 07:17:24 2025
def missing_correction(y,d,K=None,min_obs=None):
    M = 1-np.isnan(y.unstack('j'))  # Non-missing
    M = M.stack()

    M,d = prepare_data(M,d,min_obs=min_obs)

    R =  estimation(M,d,K=K,return_se=False)

    Mhat = predict_y(R['pi'],R['Ar'],R['gamma_d'],R['beta'],R['w'])

    R['M'] = M
    R['Mhat'] = Mhat

    e = M - Mhat
    R['R2'] = 1-e.var()/M.var()

    return e,R
# Construct Missing "correction":1 ends here

# [[file:../Empirics/regression.org::*Validate][Validate:1]]
# Tangled on Mon Aug 11 07:17:24 2025

def validate(y,pi,Ar,d,w,beta,gamma,GramSchmidt=False):
    def ols(x):
        y = x['y']
        x = x.drop('y',axis=1)

        y,x = drop_missing([y,x])

        b = np.linalg.lstsq(x,y,rcond=None)[0]

        return pd.Series(b.squeeze(),index=x.columns)

    X = pd.merge(Ar.reset_index('j'),pi,on=['t','m']).reset_index().set_index(['t','m','j'])

    if gamma.index.name=='tau':
        gamma_d = pd.DataFrame(d).join(gamma,on='tau')
        gamma_d.columns.name = 'j'
        gamma_d = gamma_d.drop('tau',axis=1)
        gamma_d = gamma_d.stack()
    else:
        gamma_d = inner(d,gamma,['i','t','m','j'],[])

    gamma_d.name = 'gamma_d'
    gamma_d = gamma_d[y.index]

    if GramSchmidt:
        gamma_d = Mp(gamma_d)

    if 'j' in gamma_d.index.names:
        X = pd.merge(X,gamma_d.reset_index(['i']),left_on=['t','m','j'],right_on=['t','m','j'],how='outer')
    else:
        X = pd.merge(X.reset_index('j'),gamma_d.reset_index(['i']),left_on=['t','m'],right_on=['t','m'],how='outer')

    X = X.rename(columns={('i',''):'i'}) # Deal with bug in reset_index for sparse matrices?

    X = X.reset_index().set_index(['i','t','m','j'])

    w.name='w'

    bw = outer(w,beta).stack()
    bw.name = 'bw'

    if GramSchmidt:
        MpMd = lambda x: Md_generator(x,d,Mp=True)
        bw = Mp(MpMd(bw))
        bw.name = 'bw'

    X = X.join(bw[y.index])

    X['y'] = y
    X = X.dropna()
    X.columns.name = 'l'

    B = X.groupby('j').apply(lambda x: ols(x))

    return B,X
# Validate:1 ends here

# [[file:../Empirics/regression.org::regression_class][regression_class]]
# Tangled on Mon Aug 11 07:17:24 2025
import numpy as np
import pandas as pd
import warnings
from pathlib import Path
from collections import namedtuple, OrderedDict
from cfe.df_utils import is_none

# Names of Series & DataFrames which are attributes of a Regression object

arrs = {'y':('itmj',),      # Log expenditures, (itm,j)
        'd':('itm','k'),      # Household characteristics (itm,k)
        'alpha':("j",),
        'beta':("j",),   # Frisch elasticities, (j,)
        'gamma':('j','k'),  # Coefficients on characteristics (k,)
        'alpha_se':('j',),
        'beta_se':('j',),
        'gamma_se':('j','k'),
        'beta_V':('j','jp'),
        'w':('itm',),
        'yhat':('itmj',),
        'e':('itmj',),
        'pi':('t','m'),
        'pi_se':('t','m'),
        'mults':('t','m'),
        'mults_se':('t','m'),
        'e1':('itmj',),
        'e2':('itmj',),
        'e3':('itmj',),
        'e4':('itmj',),
        'Mpw':('itm',),
        'gamma_d':('j','k'),
        'Ar':('j','tm'),
        'Ar_se':('j','tm'),
        'B':('j','l'),
        'X':('itmj','l'),
         }

class Regression:
    """
    A class which packages together data and methods for estimating a CFE demand system posed as a regression.

    Data elements (and outputs) are typically pandas Series or DataFrames.  Indexes are kept consistent across objects, with:
       - i :: Indexes households
       - t :: Indexes periods
       - m :: Indexes markets
       - j :: Indexes goods
       - k :: Indexes household characteristics

    Ethan Ligon                               October 2022
    """


    __slots__ = list(arrs.keys()) + ['attrs','Md','MpMd','Mp','Mpd']

    def __init__(self,
                 correct_miss=False,
                 method='linear',
                 K=None,
                 bootstrap_tol=None,
                 compute_se=False,
                 rectify=False,
                 verbose=False,
                 min_obs=30,
                 min_prop_items=0.1,
                 alltm=True,
                 Mpd=False,
                 **kwargs):
        """To load data, use cfe.read_sql() or cfe.read_pickle().

        To instantiate from data on log expenditures (y) and household
        characteristics (d), supply each as pd.DataFrames, with indices for y
        (i,t,m) and columns (j,) and for d indices (i,t,m) and columns (k,).
        """

        for k in self.__slots__:
            if k in kwargs.keys():
                setattr(self,k,kwargs[k])
            else:
                setattr(self,k,None)

        attrs={}
        attrs['correct_miss'] = correct_miss
        if K is not None:
            attrs['method'] = 'categorical'
        else:
            attrs['method'] = method
        attrs['K'] = K
        attrs['bootstrap_tol'] = bootstrap_tol
        attrs['compute_se'] = compute_se
        attrs['rectify'] = rectify
        attrs['verbose'] = verbose
        attrs['min_obs'] = min_obs
        attrs['min_prop_items'] = min_prop_items
        attrs['alltm'] = alltm
        attrs['Mpd'] = Mpd

        if self.attrs is None:
            self.attrs=attrs

        if 'y' in kwargs.keys() and 'd' in kwargs.keys():
            self.y,self.d = prepare_data(self.y,self.d,min_obs=min_obs,
                                         min_prop_items=min_prop_items,
                                         alltm=alltm)
# regression_class ends here

# [[file:../Empirics/regression.org::*Persistence][Persistence:1]]
# Tangled on Mon Aug 11 07:17:24 2025
    def to_pickle(self,fn):
        """
        Write dictionary of attributes to a pickle.
        """
        d = {}
        for attr in self.__dir__():
            try:
                x = getattr(self,attr)
                x.shape
                d[attr] = x
            except AttributeError: continue

        d['attrs'] = self.attrs.copy()

        #with open(fn,'wb') as f:
        #    pickle.dump(d,f)
        pd.to_pickle(d,fn)
# Persistence:1 ends here

# [[file:../Empirics/regression.org::*Accessors][Accessors:1]]
# Tangled on Mon Aug 11 07:17:24 2025
    def get_Mpdy(self):
        """Residualize y, conditioning joint on p (via time-market-good fes) and d.
        """

        Mpdy,Md,Mpd,d = estimate_MpMdy(self.y,self.d,self.attrs['K'],Mpd=True)

        self.Mpd = Mpd

        return Mpdy

    def get_MpMdy(self):
        """Residualize y, conditioning sequentially on d and then p (via time-market-good fes).
        """

        MpMdy,Md,MpMd,d = estimate_MpMdy(self.y,self.d,self.attrs['K'],Mpd=False)

        self.d = d

        self.MpMd = MpMd
        self.Md = Md

        return MpMdy

    def get_beta(self,verbose=None,compute_se=None,bootstrap_tol=1e-2,heteroskedastic=False):
        """
        Return beta.

        If estimate_se=True, compute standard errors and Variance matrix as a side-effect.
        """

        if 'Mpd' in self.attrs and self.attrs['Mpd']:
            residualize = self.get_Mpdy
        else:
            residualize = self.get_MpMdy

        if compute_se is None:
            compute_se = self.attrs['compute_se']

        if not compute_se:
            if self.beta is not None:
                return self.beta

        if compute_se:
            if self.beta_se is not None:
                return self.beta # Always return beta!

        # If we get here, we want to compute beta_se, and haven't yet.

        if verbose is None:
            verbose = self.attrs['verbose']

        b, seb, V = estimate_beta(residualize(),verbose=verbose,return_se=compute_se,bootstrap_tol=bootstrap_tol,heteroskedastic=heteroskedastic)
        b = b.squeeze()
        if seb is not None:
            self.beta_se = seb.squeeze()
            self.beta_V = V

        self.beta = b

        return self.beta

    def get_beta_se(self,verbose=None,bootstrap_tol=1e-2,heteroskedastic=False):
        """
        Return estimated standard errors of beta.

        If estimate_se=True, compute standard errors and Variance matrix as a side-effect.
        """
        if self.beta_se is not None:
            return self.beta_se # Always return beta!

        b = self.get_beta(compute_se=True)

        return self.beta_se

    def w_se(self):
        """Compute standard errors of estimated ws.
        """
        beta = self.get_beta()

        if self.e3 is None: self.get_w()

        v = w_var(self.e3,beta)

        return np.sqrt(v)


    def get_gamma_d(self,verbose=None,Mpd=None):

        if self.gamma_d is not None:
            return self.gamma_d

        if Mpd is None and 'Mpd' in self.attrs:
            Mpd = self.attrs['Mpd']
        else:
            Mpd = False # Legacy

        gamma_d,gamma = Ed(self.y,self.d,method=self.attrs['method'])

        self.gamma_d = gamma_d
        self.gamma = gamma

        self.e2 = self.y - gamma_d

        return self.gamma_d

    def get_gamma(self,verbose=None):

        if self.gamma is not None:
            return self.gamma
        else:
            gd = self.get_gamma_d(verbose=verbose)
            return self.gamma

    def get_w(self,verbose=None):
        """
        Estimate welfare weights $w$.
        """
        if self.w is not None:
            return self.w

        if verbose is None:
            verbose = self.attrs['verbose']

        gamma_d = self.get_gamma_d(verbose=verbose,Mpd=False)

        y0 = (Mpi(self.y - gamma_d)).dropna()

        b = self.get_beta(verbose=verbose)

        w,Ar,Ar_se,e3 = estimate_w(y0,b,verbose=verbose)

        self.w = w
        if self.Ar is None: self.Ar = Ar
        if self.Ar_se is None: self.Ar_se = Ar_se
        if self.e3 is None: self.e3 = e3

        return self.w

    def get_Ar(self,verbose=None):
        """
        Estimate relative prices.
        """
        if self.Ar is not None:
            return self.Ar

        if verbose is None:
            verbose = self.attrs['verbose']

        # Estimation of w also computes Ar
        self.get_w(verbose=verbose)

        return self.Ar


    def get_pi(self,verbose=None):
        """
        Estimate price index.
        """
        if self.pi is not None:
            return self.pi

        if verbose is None:
            verbose = self.attrs['verbose']

        b = self.get_beta(verbose=None)
        gamma_d = self.get_gamma_d(verbose=verbose)

        w = self.get_w(verbose=verbose)

        Ar = self.get_Ar(verbose=verbose)

        hatpi, pi_se, e4 = estimate_pi(self.y,b,w,Ar,gamma_d,verbose=verbose)
        self.pi = hatpi
        self.pi_se = pi_se
        self.e4 = e4

        return self.pi


    def get_predicted_log_expenditures(self,fill_missing=True,verbose=None):
        """
        Expected log expenditures.

        - fill_missing :: Make predictions even when observations on actual log expenditures are missing.  Default True.
        - verbose :: Default False.
        """
        if self.yhat is not None:
            if fill_missing:
                return self.yhat
            else:
                return (self.yhat + self.y*0).dropna()

        if verbose is None:
            verbose = self.attrs['verbose']

        gamma_d = self.get_gamma_d(verbose=verbose)

        b = self.get_beta(verbose=verbose)

        w = self.get_w(verbose=verbose)

        Ar = self.get_Ar(verbose=verbose)

        pi = self.get_pi(verbose=verbose)

        self.yhat = predict_y(pi,Ar,gamma_d,b,w)

        if fill_missing:
            return self.yhat
        else:
            return (self.yhat + self.y*0).dropna()

    def get_gamma_se(self):
        if self.gamma_se is not None: return self.gamma_se

        e = self.y - self.get_predicted_log_expenditures(fill_missing=False)

        assert np.abs(e.mean()<1e-10)

        d = self.d

        sigma2 = e.unstack('j').var()

        if self.attrs['method']=='linear':
            if 'Constant' not in d.columns: d['Constant'] = 1
            try:
                self.gamma_se = 1/np.sqrt((d.groupby('j').count()*(d.groupby('j').var() + d.groupby('j').mean()**2)).divide(sigma2,level='j',axis=0))
            except KeyError:  # d doesn't vary with j?
                self.gamma_se = np.sqrt((outer(sigma2,1/((d.var()+d.mean()**2)*d.count()))))

        return self.gamma_se
# Accessors:1 ends here

# [[file:../Empirics/regression.org::*Validation][Validation:1]]
# Tangled on Mon Aug 11 07:17:24 2025
    def validate(self,rectify=False,GramSchmidt=False,verbose=False):
        B,X = validate(self.y,
                       self.pi,
                       self.Ar,
                       self.d,
                       self.w,
                       self.beta,
                       self.gamma,
                       GramSchmidt=GramSchmidt)

        # Re-orthogonalize
        if rectify:
            self.yhat = None
            self.beta = self.beta*B['bw']
            if self.beta_se is not None:
                self.beta_se = self.beta_se*B['bw']
            self.Ar = self.Ar*B['Ar']
            self.Ar_se = self.Ar_se*B['Ar']
            self.pi = self.pi*(B['pi']@self.y.groupby('j').count()/self.y.shape[0])
            self.pi_se = self.pi_se*np.abs(B['pi']@self.y.groupby('j').count()/self.y.shape[0])
            try:
                self.gamma = (self.gamma.stack()*B['gamma_d']).unstack('k')
                if self.gamma_se is not None:
                    self.gamma_se = (self.gamma_se.stack()*np.abs(B['gamma_d'])).unstack('k')
            except AttributeError:
                self.gamma = self.gamma*B['gamma_d']
                if self.gamma_se is not None:
                    self.gamma_se = self.gamma_se*np.abs(B['gamma_d'])
        return B
# Validation:1 ends here

# [[file:../Empirics/regression.org::*Measures of Fit][Measures of Fit:1]]
# Tangled on Mon Aug 11 07:17:24 2025

    def mse(self):
        """
        Mean-squared error of estimates.
        """
        if self.yhat is None:
            self.get_predicted_log_expenditures()
        try:
            return ((self.y - self.yhat)**2).mean()
        except AttributeError:
            self.get_predicted_log_expenditures()
            return mse(self)

    def R2(self,summary=False):
        yhat = self.get_predicted_log_expenditures(fill_missing=False)

        e = self.y - yhat.reindex_like(self.y)

        if summary:
            sigma2 = e.var()

            R2 = 1 - sigma2/self.y.var()
        else:
            sigma2 = e.unstack('j').var()

            R2 = 1 - sigma2/self.y.unstack('j').var()

        return R2
# Measures of Fit:1 ends here

# [[file:../Empirics/regression.org::*Find optimal number of clusters][Find optimal number of clusters:1]]
# Tangled on Mon Aug 11 07:17:24 2025
    def optimal_number_of_clusters(self):
        """
        Find optimal number of clusters for K-means.
        """
        self.flags['K'] = find_optimal_K(self.y,self.d)
# Find optimal number of clusters:1 ends here

# [[file:../Empirics/regression.org::*Predicted Expenditures][Predicted Expenditures:1]]
# Tangled on Mon Aug 11 07:17:24 2025
    def predicted_expenditures(self,resample=False,clusterby=['t','m','j'],fill_missing=True,verbose=False):
        """Compute predicted /levels/ of expenditures.

        This is different from exp(yhat), since we have to account for the expected value of exp(e), where e = y - yhat.

        One standard (and the default) way to calculate these is by assuming that the distribution of e is normal.  An alternative is to resample residuals.

        Regardless of whether resampling is chosen, means (and variances) are selected at the level of the list clusterby.
        """
        if self.yhat is None:
            self.yhat = self.get_predicted_log_expenditures(fill_missing=True,verbose=verbose)

        e = self.y - self.yhat
        eg = e.dropna().groupby(clusterby)

        if not resample:
            # Use iqr instead of variance for some robustness to outliers
            # Relation for normal dist: iqr/1.3489795 = sigma
            evar = (eg.transform(iqr)/1.3489795)**2
        else:
            if resample < 1: # Assume this is a tolerance
                tol = resample
            last = -1
            evar = e.dropna().groupby(clusterby).transform(np.var)
            evar = evar.sort_index(level=clusterby)
            i = 0
            diff = 1
            while diff>tol:
                last = evar
                esample = eg.sample(frac=1,replace=True)
                drawvar = (esample.groupby(clusterby).transform(iqr)/1.3489795)**2
                evar = i/(i+1)*evar + drawvar.values/(i+1)
                i += 1
                diff = np.abs(evar-last).max()
                if verbose: print(f'Draw {i}, diff={diff}')

        if fill_missing:
            evar = evar.groupby(clusterby).mean()
            xhat = np.exp(self.yhat.add(evar/2))
            xhat = xhat.reorder_levels(self.yhat.index.names).sort_index()
        else:
            xhat = np.exp(self.yhat + evar/2)
            xhat = xhat.reorder_levels(self.yhat.index.names).sort_index()

        return xhat
# Predicted Expenditures:1 ends here

# [[file:../Empirics/regression.org::*Predicted \lambda][Predicted \lambda:1]]
# Tangled on Mon Aug 11 07:17:24 2025
    def predicted_lambda(self):
        """Expected value of minus the antilog of $w$.
        """
        v = self.w_se()**2
        lhat = np.exp(-self.w + v/2)

        return lhat
# Predicted \lambda:1 ends here

# [[file:../Empirics/regression.org::*Average Estimator of =w=][Average Estimator of =w=:1]]
# Tangled on Mon Aug 11 07:17:24 2025
    def average_to_get_w(self,weight=False):
        e = self.get_Mpdy()
        if weight:
            sigmaj = e.groupby('j').transform('std')
        else:
            sigmaj = 1
        w = (e/sigmaj).groupby(['i','t','m']).mean()

        return w
# Average Estimator of =w=:1 ends here

# [[file:../Empirics/regression.org::*Estimate Everything][Estimate Everything:1]]
# Tangled on Mon Aug 11 07:17:24 2025
    def estimate_all(self,verbose=None,heteroskedastic=False):
        warnings.warn(
            "estimate_all is deprecated. Use other methods, e.g. get_pi instead.",
            DeprecationWarning,
            stacklevel=2
        )

        lhs = self.y
        # 1. Estimate gamma
        gamma_d,gamma = Ed(lhs,self.d,method=self.attrs['method'])

        MpMdy,Md,MpMd,d = estimate_MpMdy(lhs,self.d,self.attrs['K'])

        # 2. Estimate beta
        b = estimate_beta(MpMdy,verbose=verbose,return_se=False,heteroskedastic=heteroskedastic).squeeze()

        # 3. Estimate w
        y0 = (Mpi(self.y - gamma_d)).dropna()

        w,Ar,Ar_se,e3 = estimate_w(y0,b,verbose=verbose)
        # 4. Estimate Ar
        # 5. Estimate pi
        # 6. Estimate standard errors
# Estimate Everything:1 ends here

# [[file:../Empirics/regression.org::*Presentation methods][Presentation methods:1]]
# Tangled on Mon Aug 11 07:17:24 2025
    def graph_beta(self,fn=None,xlabel='Frisch Elasticities',heteroskedastic=False):
        import matplotlib.pyplot as plt

        if self.beta is None or self.beta_se is None:
            self.get_beta(compute_se=True,heteroskedastic=heteroskedastic)

        beta = self.beta.sort_values()
        se = self.beta_se

        # Sort se to match beta
        se = se[beta.index]

        # Want about 1/8" vertical space per good
        fig,ax = plt.subplots(figsize=(8,1+len(beta)/7))

        ax.errorbar(beta,range(len(beta)), xerr=se)
        ax.set_xlabel(xlabel)

        ax.set_yticks(list(range(len(beta))))
        ax.set_yticklabels(beta.index.values.tolist(),rotation=0,size='small')

        fig.tight_layout()

        if fn is not None:
            fig.savefig(fn,bbox_inches='tight')

        return fig
# Presentation methods:1 ends here

# [[file:../Empirics/regression.org::regression_demand_interface][regression_demand_interface]]
# Tangled on Mon Aug 11 07:17:24 2025
import consumerdemands
import pandas as pd

def _demand_parameters(self,p=None,d=None):
    """Return tuple of p and dictionary of (alpha,beta,phi) from regression instance.

    Suitable for passing to =cfe.demand= functions.
    """

    beta = self.beta
    n = len(beta)

    if d is None:
        gd = self.get_gamma_d().groupby('j').mean()
    else:
        gd = d@self.gamma.T

    alpha = np.exp(gd)

    if p is None or len(p)==0:
        prices = np.exp((self.pi + self.Ar).groupby('j').mean())
    else:
        prices = p

    assert len(prices), f"What happened to prices? p={prices}."

    phi = 0 # phi not (yet?) an attribute of Regression.

    # Cast to numeric arrays
    try:
        prices = prices.values
    except AttributeError:
        pass

    try:
        alpha = alpha.values
    except AttributeError:
        pass
    try:
        beta = beta.values
    except AttributeError:
        pass

    try:
        phi = phi.values
    except AttributeError:
        pass

    return prices,{'alpha':alpha,'beta':beta,'phi':phi}

def _lambdavalue(self,x,p=None,z=None):
    """Marginal utility at expenditures x.
    """

    p,pparms = _demand_parameters(self,p,z)

    return consumerdemands.lambdavalue(x,p,pparms)

def _demands(self,x,p=None,z=None,type="Marshallian"):
    """Quantities demanded at prices p for household with observable
    characteristics z, having a utility function with parameters given
    by (possibly estimated) attributes from a Regression (i.e., the
    vectors of parameters alpha, beta, delta).

    Default type is "Marshallian", in which case argument x is budget.

    Alternative types:
       - "Frischian" :: argument x is Marginal utility of expenditures
       - "Hicksian" :: argument x is level of utility

    Ethan Ligon                                    April 2019
    """

    idx = self.get_beta().index
    p,pparms = _demand_parameters(self,p,z)

    Qs = {'Marshallian':consumerdemands.marshallian.demands,
          'Hicksian':consumerdemands.hicksian.demands,
          'Frischian':consumerdemands.frischian.demands}

    q = pd.Series(Qs[type](x,p,pparms),index=idx,name='quantities')

    return q

def _expenditures(self,x,p=None,z=None,type='Marshallian'):
    """Expenditures for different goods at prices p for household with observable
    characteristics z, having a utility function with parameters given
    by (possibly estimated) attributes from a Regression (i.e., the
    vectors of parameters alpha, beta, delta).

    Default type is "Marshallian", in which case argument x is budget.

    Alternative types:
       - "Frischian" :: argument x is Marginal utility of expenditures
       - "Hicksian" :: argument x is level of utility

    Ethan Ligon                                    April 2023
    """

    p,pparms = _demand_parameters(self,p,z)

    q = _demands(self,x,p=p,z=z,type=type)

    return p*q


def _utility(self,x,p=None,z=None,type="Marshallian"):
    """(Indirect) utility

    Level of utility at prices p for household with observable
    characteristics z, having a utility function with parameters given
    by (possibly estimated) attributes from a Regression (i.e., the
    vectors of parameters alpha, beta, delta).

    Default type is "Marshallian", in which case argument x is budget.

    Alternative types:
       - "Frischian" :: argument x is Marginal utility of expenditures
       - "Hicksian" :: argument x is level of utility

    Ethan Ligon                                    April 2019
    """

    p,pparms = _demand_parameters(self,p,z)

    Us = {'Marshallian':consumerdemands.marshallian.indirect_utility,
          'Hicksian': lambda U,**xargs: U,
          'Frischian':consumerdemands.frischian.indirect_utility}

    return Us[type](x,p,pparms)

def _expenditurefunction(self,x,p=None,z=None,type='Hicksian'):
    """Total Expenditures

    Expenditures at prices p for household with observable
    characteristics z, having a utility function with parameters given
    by (possibly estimated) attributes from a Regression (i.e., the
    vectors of parameters alpha, beta, delta).

    Default type is "Hicksian", in which case argument x is level of utility U.

    Alternative types:
       - "Frischian" :: argument x is Marginal utility of expenditures
       - "Marshallian" :: argument x is expenditures.

    Ethan Ligon                                    April 2019
    """

    p,pparms = _demand_parameters(self,p,z)

    Xs = {'Marshallian': lambda U,**xargs: U,
          'Hicksian': consumerdemands.hicksian.expenditurefunction,
          'Frischian':consumerdemands._core.expenditures}

    return Xs[type](x,p,pparms)

def _relative_risk_aversion(self,p=None,z=None):
    """Returns relative risk aversion =function= that varies with =x=.

    Varies with prices p, and observablecharacteristics z.

    Ethan Ligon                                    December 2022
    """

    p,pparms = _demand_parameters(self,p,z)

    return consumerdemands.demands.relative_risk_aversion(p,pparms)

Regression.consumerdemands = consumerdemands
Regression.demands = _demands
Regression.expenditures = _expenditures
Regression.demand_parameters = _demand_parameters
Regression.lambdavalue = _lambdavalue
Regression.indirect_utility = _utility
Regression.expenditure = _expenditurefunction
Regression.relative_risk_aversion = _relative_risk_aversion
# regression_demand_interface ends here

# [[file:../Empirics/regression.org::*=read_pickle=][=read_pickle=:1]]
# Tangled on Mon Aug 11 07:17:24 2025
import pickle

def read_pickle(fn,cache_dir=None):
    """
    Read pickled dictionary and assign keys as attributes to Regression object.
    """
    import fsspec

    try:
        R = pickle.load(fn)  # Is fn a file?
    except TypeError:  # Maybe a filename?
        if cache_dir is not None:
            if 'filecache::' not in fn:  # May already have caching specified
                fn = 'filecache::' + fn
            storage_options = {'filecache':{'cache_dir':cache_dir}}
            with fsspec.open(fn,mode='rb',
                             storage_options=storage_options) as f:
                R = pickle.load(f)
        else:
            with fsspec.open(fn,mode='rb') as f:
                R = pickle.load(f)

    if type(R) is not dict:
        R = R.__dict__
        # Fix ill-considered attribute name
        try:
            R['mults_se'] = R['se_mult']
            del R['se_mult']
        except KeyError:
            pass

    return Regression(**R)
# =read_pickle=:1 ends here
