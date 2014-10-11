# -*- coding: utf-8 -*-

u"""
Beta regression for modeling rates and proportions.

References
----------
Grün, Bettina, Ioannis Kosmidis, and Achim Zeileis. Extended beta regression
in R: Shaken, stirred, mixed, and partitioned. No. 2011-22. Working Papers in
Economics and Statistics, 2011.

Smithson, Michael, and Jay Verkuilen. "A better lemon squeezer?
Maximum-likelihood regression with beta-distributed dependent variables."
Psychological methods 11.1 (2006): 54.
"""
from __future__ import print_function
import numpy as np
import pandas as pd
import statsmodels.api as sm
import patsy

from scipy.special import gammaln as lgamma

from statsmodels.base.model import GenericLikelihoodModel
from statsmodels.genmod.families import Binomial

Logit = sm.families.links.logit

_init_example = """

    Beta regression with default of logit-link for exog and log-link
    for precision.

    >>> mod = Beta(endog, exog)
    >>> rslt = mod.fit()
    >>> print(rslt.summary())

    We can also specify a formula and a specific structure and use the
    identity-link for precision.

    >>> from sm.families.links import identity
    >>> Z = patsy.dmatrix('~ temp', dat, return_type='dataframe')
    >>> mod = Beta.from_formula('iyield ~ C(batch, Treatment(10)) + temp',
    ...                         dat, exog_precision=Z, link_precision=identity())

    In the case of proportion-data, we may think that the precision depends on
    the number of measurements. E.g for sequence data, on the number of
    sequence reads covering a site:

    >>> Z = patsy.dmatrix('~ coverage', df)
    >>> mod = Beta.from_formula('methylation ~ disease + age + gender + coverage', df, Z)
    >>> rslt = mod.fit()

"""

class Beta(GenericLikelihoodModel):

    """Beta Regression.

    This implementation uses a `precision` parameter
    """

    def __init__(self, endog, exog, exog_precision=None, link=Logit(),
            link_precision=sm.families.links.Log(), **kwds):
        """
        Parameters
        ----------
        endog : array-like
            1d array of endogenous values (i.e. responses, outcomes,
            dependent variables, or 'Y' values).
        exog : array-like
            2d array of exogeneous values (i.e. covariates, predictors,
            independent variables, regressors, or 'X' values). A nobs x k
            array where `nobs` is the number of observations and `k` is
            the number of regressors. An intercept is not included by
            default and should be added by the user. See
            `statsmodels.tools.add_constant`.
        exog_precision : array-like
            2d array of variables for the precision.
        link : link
            Any link in sm.families.links for `exog`
        link_precision : link
            Any link in sm.families.links for `exog_precision`

        Examples
        --------
        {example}

        See Also
        --------
        :ref:`links`

        """.format(example=_init_example)
        etmp = np.array(endog)
        assert np.all((0 < etmp) & (etmp < 1))
        if exog_precision is None:
            extra_names = ['precision']
            exog_precision = np.ones((len(endog), 1), dtype='f')
        else:
            extra_names = ['precision-%s' % zc for zc in \
                    (exog_precision.columns \
                    if hasattr(exog_precision, 'columns')
                    else range(1, exog_precision.shape[1] + 1))]

        kwds['extra_params_names'] = extra_names

        super(Beta, self).__init__(endog, exog, **kwds)
        self.link = link
        self.link_precision = link_precision

        self.exog_precision = exog_precision
        assert len(self.exog_precision) == len(self.endog)

    @classmethod
    def from_formula(cls, formula, data, exog_precision_formula=None,
                     *args, **kwargs):
        if exog_precision_formula is not None:
            if 'subset' in kwargs:
                d = data.ix[kwargs['subset']]
                Z = patsy.dmatrix(exog_precision_formula, d)
            else:
                Z = patsy.dmatrix(exog_precision_formula, data)
            kwargs['exog_precision'] = Z  

        return super(Beta, cls).from_formula(formula, data, *args,
                                      **kwargs)


    def nloglikeobs(self, params):
        """
        Negative log-likelihood.

        Parameters
        ----------

        params : np.ndarray
            Parameter estimates
        """
        return -self._ll_br(self.endog, self.exog, self.exog_precision, params)

    def _ll_br(self, y, X, Z, params):
        nz = Z.shape[1]

        Xparams = params[:-nz]
        Zparams = params[-nz:]

        mu = self.link.inverse(np.dot(X, Xparams))
        phi = self.link_precision.inverse(np.dot(Z, Zparams))

        alpha = mu * phi
        beta = (1 - mu) * phi

        if np.any(alpha <= np.finfo(float).eps): return np.array(-np.inf)
        if np.any(beta <= np.finfo(float).eps): return np.array(-np.inf)

        ll = lgamma(phi) - lgamma(mu * phi) - lgamma((1 - mu) * phi) \
                + (mu * phi - 1) * np.log(y) + (((1 - mu) * phi) - 1) \
                * np.log(1 - y)

        return ll


    def score(self, params):
        """
        Returns the score vector of the profile log-likelihood.

        http://www.tandfonline.com/doi/pdf/10.1080/00949650903389993
        """
        sf = self.score_factor(params)

        d1 = np.dot(sf[:, 0], self.exog)
        d2 = np.dot(sf[:, 1], self.exog_precision)
        return np.concatenate((d1, d2))


    def score_check(self, params):
        """inherited score with finite differences
        """
        return super(Beta, self).score(params)


    def score_factor(self, params):
        """derivative of loglikelihood function without the exog

        This needs to be multiplied with the exog to obtain the score_obs
        """
        from scipy import special
        digamma = special.psi

        y, X, Z = self.endog, self.exog, self.exog_precision
        nz = Z.shape[1]
        Xparams = params[:-nz]
        Zparams = params[-nz:]

        # NO LINKS
        mu = self.link.inverse(np.dot(X, Xparams))
        phi = self.link_precision.inverse(np.dot(Z, Zparams))

        ystar = np.log( y / (1. - y))
        mustar = digamma(mu * phi) - digamma((1 - mu) * phi)
        yt = np.log(1 - y)
        mut = digamma((1 - mu) * phi) - digamma(phi)

        t = 1. / self.link.deriv(mu)
        h = 1. / self.link_precision.deriv(phi)
        #
        sf1 = phi * t * (ystar - mustar)
        sf2 = h * ( mu * (ystar - mustar) + yt - mut)

        return np.column_stack((sf1, sf2))


    def score_hessian_factor(self, params, return_hessian=False, observed=True):
        """derivatives of loglikelihood function without the exog

        This needs to be multiplied with the exog to obtain the score_obs

        This calculates score and hessian factors at the same time, since there
        is a large overlap in calculations
        """
        from scipy import special
        digamma = special.psi

        y, X, Z = self.endog, self.exog, self.exog_precision
        nz = Z.shape[1]
        Xparams = params[:-nz]
        Zparams = params[-nz:]

        # NO LINKS
        mu = self.link.inverse(np.dot(X, Xparams))
        phi = self.link_precision.inverse(np.dot(Z, Zparams))

        ystar = np.log( y / (1. - y))
        mustar = digamma(mu * phi) - digamma((1 - mu) * phi)
        yt = np.log(1 - y)
        mut = digamma((1 - mu) * phi) - digamma(phi)

        t = 1. / self.link.deriv(mu)
        h = 1. / self.link_precision.deriv(phi)

        ymu_star = (ystar - mustar)
        sf1 = phi * t * ymu_star
        sf2 = h * ( mu * ymu_star + yt - mut)

        if return_hessian:
            trigamma = lambda x: special.polygamma(1, x)
            var_star = trigamma(mu * phi) + trigamma((1 - mu) * phi)
            var_t = trigamma((1 - mu) * phi) - trigamma(phi)

            c = - trigamma((1 - mu) * phi)
            s = self.link.deriv2(mu)
            q = self.link_precision.deriv2(phi)


            jbb = (phi * t) * var_star
            if observed:
                jbb += s * t**2 * ymu_star

            jbb *= t * phi

            jbg = phi * t * h * (mu * var_star + c)
            if observed:
                jbg -= ymu_star * t * h

            jgg = h**2 * (mu**2 * var_star + 2 * mu * c + var_t)
            if observed:
                jgg += (mu * ymu_star + yt - mut) * q * h**3    # **3 ?

        return np.column_stack((sf1, sf2)), (-jbb, -jbg, -jgg)


    def score_obs(self, params):
        sf = self.score_factor(params)

        # elementwise product for each row (observation)
        d1 = sf[:, :1] * self.exog
        d2 = sf[:, 1:2] * self.exog_precision
        return np.column_stack((d1, d2))


    def hessian_1(self, params, observed=True):
        _, hf = self.score_hessian_factor(params, return_hessian=True,
                                          observed=observed)

        hf11, hf12, hf22 = hf

        # elementwise product for each row (observation)
        d11 = (self.exog.T * hf11).dot(self.exog)
        d12 = (self.exog.T * hf12).dot(self.exog_precision)
        d22 = (self.exog_precision.T * hf22).dot(self.exog_precision)
        return np.bmat([[d11, d12], [d12.T, d22]]).A



    def fit(self, start_params=None, maxiter=100000, maxfun=5000, disp=False,
            method='bfgs', **kwds):
        """
        Fit the model.

        Parameters
        ----------
        start_params : array-like
            A vector of starting values for the regression
            coefficients.  If None, a default is chosen.
        maxiter : integer
            The maximum number of iterations
        disp : bool
            Show convergence stats.
        method : str
            The optimization method to use.
        """

        if start_params is None:
            start_fit = sm.OLS(self.link(self.endog), self.exog,
                                  ).fit(disp=False)
            start_params = start_fit.params
            nz = self.exog_precision.shape[1]
            # http://www.ime.usp.br/~sferrari/beta.pdf suggests starting phi
            # on page 8
            start_params = np.append(start_params, [0.5 / nz] * nz)

        return super(Beta, self).fit(start_params=start_params,
                                        maxiter=maxiter, maxfun=maxfun,
                                        method=method, disp=disp, **kwds)

if __name__ == "__main__":

    import patsy

    fex = pd.read_csv('tests/foodexpenditure.csv')
    m = Beta.from_formula(' I(food/income) ~ income + persons', fex)
    print(m.fit().summary())
    #print GLM.from_formula('iyield ~ C(batch) + temp', dat, family=Binomial()).fit().summary()

    dev = pd.read_csv('tests/methylation-test.csv')
    Z = patsy.dmatrix('~ age', dev, return_type='dataframe')
    m = Beta.from_formula('methylation ~ gender + CpG', dev,
            exog_precision=Z,
            link_precision=sm.families.links.identity())
    print(m.fit().summary())