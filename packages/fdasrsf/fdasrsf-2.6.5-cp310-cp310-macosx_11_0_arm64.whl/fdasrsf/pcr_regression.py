"""
Warping Invariant PCR Regression using SRSF

moduleauthor:: J. Derek Tucker <jdtuck@sandia.gov>

"""

import numpy as np
import fdasrsf as fs
import fdasrsf.utility_functions as uf
import fdasrsf.fPCA as fpca
import fdasrsf.regression as rg
import fdasrsf.geometry as geo
from scipy.linalg import inv
from scipy.stats import t
from scipy.optimize import fmin_l_bfgs_b


class elastic_pcr_regression:
    """
    This class provides elastic pcr regression for functional data using the
    SRVF framework accounting for warping

    Usage:  obj = elastic_pcr_regression(f,y,time)

    :param f: (M,N) % matrix defining N functions of M samples
    :param y: response vector of length N
    :param warp_data: fdawarp object of alignment
    :param pca: class dependent on fPCA method used object of fPCA
    :param alpha: intercept
    :param b: coefficient vector
    :param SSE: sum of squared errors

    Author :  J. D. Tucker (JDT) <jdtuck AT sandia.gov>
    Date   :  18-Mar-2018
    """

    def __init__(self, f, y, time):
        """
        Construct an instance of the elastic_pcr_regression class
        :param f: numpy ndarray of shape (M,N) of N functions with M samples
        :param y: response vector
        :param time: vector of size M describing the sample points
        """
        a = time.shape[0]

        if f.shape[0] != a:
            raise Exception("Columns of f and time must be equal")

        self.f = f
        self.y = y
        self.time = time

    def calc_model(
        self,
        pca_method="combined",
        no=5,
        var_exp=None,
        smooth_data=False,
        sparam=25,
        parallel=False,
        C=None,
    ):
        """
        This function identifies a regression model with phase-variability
        using elastic pca

        :param pca_method: string specifying pca method (options = "combined",
                        "vert", or "horiz", default = "combined")
        :param no: scalar specify number of principal components (default=5)
        :param var_exp: compute no based on value percent variance explained
                        (example: 0.95)
        :param smooth_data: smooth data using box filter (default = F)
        :param sparam: number of times to apply box filter (default = 25)
        :param parallel: run in parallel (default = F)
        :param C: scale balance parameter for combined method (default = None)
        """

        if smooth_data:
            self.f = fs.smooth_data(self.f, sparam)

        N1 = self.f.shape[1]

        # Align Data
        self.warp_data = fs.fdawarp(self.f, self.time)
        self.warp_data.srsf_align(parallel=parallel)

        # Calculate PCA
        if pca_method == "combined":
            self.pca = fpca.fdajpca(self.warp_data)
        elif pca_method == "vert":
            self.pca = fpca.fdavpca(self.warp_data)
        elif pca_method == "horiz":
            self.pca = fpca.fdahpca(self.warp_data)
        else:
            raise Exception("Invalid fPCA Method")
        self.pca.calc_fpca(no=no, var_exp=var_exp)

        no = self.pca.no

        # OLS using PCA basis
        lam = 0
        R = 0
        Phi = np.ones((N1, no + 1))
        Phi[:, 1:(no + 1)] = self.pca.coef
        xx = np.dot(Phi.T, Phi)
        inv_xx = inv(xx + lam * R)
        xy = np.dot(Phi.T, self.y)
        b = np.dot(inv_xx, xy)
        alpha = b[0]
        b = b[1:no + 1]

        # compute the SSE
        int_X = np.zeros(N1)
        for ii in range(0, N1):
            int_X[ii] = np.sum(self.pca.coef[ii, :] * b)

        y_pred = alpha + int_X
        SSE = np.sum((self.y - y_pred) ** 2)

        self.Ntr = len(self.y)
        stdev = np.sqrt(sum((y_pred - self.y) ** 2) / (self.Ntr - 2))

        self.alpha = alpha
        self.b = b
        self.SSE = SSE
        self.stdev = stdev
        self.pca_method = pca_method

        return

    def predict(self, newdata=None, alpha=0.05):
        """
        This function performs prediction on regression model on new
        data if available or current stored data in object
        Usage:  obj.predict(newdata)

        :param newdata: dict containing new data for prediction (needs
                        the keys below, if None predicts on training data)
        :type newdata: dict
        :param f: (M,N) matrix of functions
        :param time: vector of time points
        :param y: truth if available
        :param smooth: smooth data if needed
        :param sparam: number of times to run filter
        """

        if newdata is not None:
            f = newdata["f"]
            n = f.shape[1]
            y = newdata["y"]
            if newdata["smooth"]:
                sparam = newdata["sparam"]
                f = fs.smooth_data(f, sparam)
            
            self.pca.project(f)
            a = self.pca.new_coef

            self.y_int = np.zeros((n, 2))
            X = inv(self.pca.coef.T @ self.pca.coef)
            df = self.Ntr - self.pca.coef.shape[1] - 1
            self.y_pred = np.zeros(n)
            for ii in range(0, n):
                self.y_pred[ii] = self.alpha + np.dot(a[ii, :], self.b)
                interval = (
                    t.ppf(alpha / 2, df)
                    * self.stdev
                    * np.sqrt(1 + a[ii, :] @ X @ a[ii, :])
                )
                self.y_int[ii, 0] = interval
                self.y_int[ii, 1] = -interval

            if y is None:
                self.SSE = np.nan
            else:
                self.SSE = np.sum((y - self.y_pred) ** 2)
        else:
            n = self.pca.coef.shape[0]
            self.y_pred = np.zeros(n)
            self.y_int = np.zeros((n, 2))
            X = inv(self.pca.coef.T @ self.pca.coef)
            df = self.Ntr - self.pca.coef.shape[1] - 1
            for ii in range(0, n):
                self.y_pred[ii] = self.alpha + np.dot(self.pca.coef[ii, :], self.b)
                interval = (
                    t.ppf(alpha / 2, df)
                    * self.stdev
                    * np.sqrt(1 + self.pca.coef[ii, :] @ X @ self.pca.coef[ii, :])
                )
                self.y_int[ii, 0] = interval
                self.y_int[ii, 1] = -interval

            self.SSE = np.sum((self.y - self.y_pred) ** 2)

        return


class elastic_lpcr_regression:
    """
    This class provides elastic logistic pcr regression for functional
    data using the SRVF framework accounting for warping

    Usage:  obj = elastic_lpcr_regression(f,y,time)

    :param f: (M,N) % matrix defining N functions of M samples
    :param y: response vector of length N (-1/1)
    :param warp_data: fdawarp object of alignment
    :param pca: class dependent on fPCA method used object of fPCA
    :param information:
    :param alpha: intercept
    :param b: coefficient vector
    :param Loss: logistic loss
    :param PC: probability of classification
    :param ylabels: predicted labels

    Author :  J. D. Tucker (JDT) <jdtuck AT sandia.gov>
    Date   :  18-Mar-2018
    """

    def __init__(self, f, y, time):
        """
        Construct an instance of the elastic_lpcr_regression class
        :param f: numpy ndarray of shape (M,N) of N functions with M samples
        :param y: response vector
        :param time: vector of size M describing the sample points
        """
        a = time.shape[0]

        if f.shape[0] != a:
            raise Exception("Columns of f and time must be equal")

        self.f = f
        self.y = y
        self.time = time

    def calc_model(
        self, pca_method="combined", no=5, smooth_data=False, sparam=25, parallel=False
    ):
        """
        This function identifies a logistic regression model with phase-variability
        using elastic pca

        :param pca_method: string specifying pca method (options = "combined",
                        "vert", or "horiz", default = "combined")
        :param no: scalar specify number of principal components (default=5)
        :param smooth_data: smooth data using box filter (default = F)
        :param sparam: number of times to apply box filter (default = 25)
        :param parallel: calculate in parallel (default = F)
        :type f: np.ndarray
        :type time: np.ndarray
        """

        if smooth_data:
            self.f = fs.smooth_data(self.f, sparam)

        N1 = self.f.shape[1]

        # Align Data
        self.warp_data = fs.fdawarp(self.f, self.time)
        self.warp_data.srsf_align(parallel=parallel)

        # Calculate PCA
        if pca_method == "combined":
            self.pca = fpca.fdajpca(self.warp_data)
        elif pca_method == "vert":
            self.pca = fpca.fdavpca(self.warp_data)
        elif pca_method == "horiz":
            self.pca = fpca.fdahpca(self.warp_data)
        else:
            raise Exception("Invalid fPCA Method")
        self.pca.calc_fpca(no)

        # OLS using PCA basis
        lam = 0
        R = 0
        Phi = np.ones((N1, no + 1))
        Phi[:, 1 : (no + 1)] = self.pca.coef
        # Find alpha and beta using l_bfgs
        b0 = np.zeros(no + 1)
        out = fmin_l_bfgs_b(
            rg.logit_loss,
            b0,
            fprime=rg.logit_gradient,
            args=(Phi, self.y),
            pgtol=1e-10,
            maxiter=200,
            maxfun=250,
            factr=1e-30,
        )

        b = out[0]
        alpha = b[0]

        # compute the Loss
        LL = rg.logit_loss(b, Phi, self.y)

        b = b[1: no + 1]

        self.alpha = alpha
        self.b = b
        self.LL = LL
        self.pca_method = pca_method

        return

    def predict(self, newdata=None):
        """
        This function performs prediction on regression model on new data if available or current stored data in object
        Usage:  obj.predict(newdata)

        :param newdata: dict containing new data for prediction (needs the keys below, if None predicts on training data)
        :type newdata: dict
        :param f: (M,N) matrix of functions
        :param time: vector of time points
        :param y: truth if available
        :param smooth: smooth data if needed
        :param sparam: number of times to run filter
        """

        if newdata is not None:
            f = newdata["f"]
            n = f.shape[1]
            y = newdata["y"]
            if newdata["smooth"]:
                sparam = newdata["sparam"]
                f = fs.smooth_data(f, sparam)

            self.pca.project(f)
            a = self.pca.new_coef

            self.y_pred = np.zeros(n)
            for ii in range(0, n):
                self.y_pred[ii] = self.alpha + np.sum(a[ii, :] * self.b)

            if y is None:
                self.y_pred = rg.phi(self.y_pred)
                self.y_labels = np.ones(n)
                self.y_labels[self.y_pred < 0.5] = -1
                self.PC = np.nan
            else:
                self.y_pred = rg.phi(self.y_pred)
                self.y_labels = np.ones(n)
                self.y_labels[self.y_pred < 0.5] = -1
                TP = np.sum(y[self.y_labels == 1] == 1)
                FP = np.sum(y[self.y_labels == -1] == 1)
                TN = np.sum(y[self.y_labels == -1] == -1)
                FN = np.sum(y[self.y_labels == 1] == -1)
                self.PC = (TP + TN) / (TP + FP + FN + TN)
        else:
            n = self.pca.coef.shape[0]
            self.y_pred = np.zeros(n)
            for ii in range(0, n):
                self.y_pred[ii] = self.alpha + np.dot(self.pca.coef[ii, :], self.b)

            self.y_pred = rg.phi(self.y_pred)
            self.y_labels = np.ones(n)
            self.y_labels[self.y_pred < 0.5] = -1
            TP = np.sum(self.y[self.y_labels == 1] == 1)
            FP = np.sum(self.y[self.y_labels == -1] == 1)
            TN = np.sum(self.y[self.y_labels == -1] == -1)
            FN = np.sum(self.y[self.y_labels == 1] == -1)
            self.PC = (TP + TN) / (TP + FP + FN + TN)

        return


class elastic_mlpcr_regression:
    """
    This class provides elastic multinomial logistic pcr regression for functional
    data using the SRVF framework accounting for warping

    Usage:  obj = elastic_mlpcr_regression(f,y,time)

    :param f: (M,N) % matrix defining N functions of M samples
    :param y: response vector of length N
    :param Y: coded label matrix
    :param warp_data: fdawarp object of alignment
    :param pca: class dependent on fPCA method used object of fPCA
    :param information:
    :param alpha: intercept
    :param b: coefficient vector
    :param Loss: logistic loss
    :param PC: probability of classification
    :param ylabels: predicted labels

    Author :  J. D. Tucker (JDT) <jdtuck AT sandia.gov>
    Date   :  18-Mar-2018
    """

    def __init__(self, f, y, time):
        """
        Construct an instance of the elastic_mlpcr_regression class
        :param f: numpy ndarray of shape (M,N) of N functions with M samples
        :param y: response vector
        :param time: vector of size M describing the sample points
        """
        a = time.shape[0]

        if f.shape[0] != a:
            raise Exception("Columns of f and time must be equal")

        self.f = f
        self.y = y
        self.time = time
        N1 = f.shape[1]

        # Code labels
        m = y.max()
        self.n_classes = m
        self.Y = np.zeros((N1, m), dtype=int)
        for ii in range(0, N1):
            self.Y[ii, y[ii] - 1] = 1

    def calc_model(
        self, pca_method="combined", no=5, smooth_data=False, sparam=25, parallel=False
    ):
        """
        This function identifies a logistic regression model with phase-variability
        using elastic pca

        :param f: numpy ndarray of shape (M,N) of N functions with M samples
        :param y: numpy array of N responses
        :param time: vector of size M describing the sample points
        :param pca_method: string specifying pca method (options = "combined",
                        "vert", or "horiz", default = "combined")
        :param no: scalar specify number of principal components (default=5)
        :param smooth_data: smooth data using box filter (default = F)
        :param sparam: number of times to apply box filter (default = 25)
        :param parallel: run model in parallel (default = F)
        :type f: np.ndarray
        :type time: np.ndarray
        """

        if smooth_data:
            self.f = fs.smooth_data(self.f, sparam)

        N1 = self.f.shape[1]

        # Align Data
        self.warp_data = fs.fdawarp(self.f, self.time)
        self.warp_data.srsf_align(parallel=parallel)

        # Calculate PCA
        if pca_method == "combined":
            self.pca = fpca.fdajpca(self.warp_data)
        elif pca_method == "vert":
            self.pca = fpca.fdavpca(self.warp_data)
        elif pca_method == "horiz":
            self.pca = fpca.fdahpca(self.warp_data)
        else:
            raise Exception("Invalid fPCA Method")
        self.pca.calc_fpca(no)

        # OLS using PCA basis
        lam = 0
        R = 0
        Phi = np.ones((N1, no + 1))
        Phi[:, 1: (no + 1)] = self.pca.coef
        # Find alpha and beta using l_bfgs
        b0 = np.zeros(self.n_classes * (no + 1))
        out = fmin_l_bfgs_b(
            rg.mlogit_loss,
            b0,
            fprime=rg.mlogit_gradient,
            args=(Phi, self.Y),
            pgtol=1e-10,
            maxiter=200,
            maxfun=250,
            factr=1e-30,
        )

        b = out[0]
        B0 = b.reshape(no + 1, self.n_classes)
        alpha = B0[0, :]

        # compute the Loss
        LL = rg.mlogit_loss(b, Phi, self.y)

        b = B0[1: no + 1, :]

        self.alpha = alpha
        self.b = b
        self.LL = LL
        self.pca_method = pca_method

        return

    def predict(self, newdata=None):
        """
        This function performs prediction on regression model on new data if available or current stored data in object
        Usage:  obj.predict(newdata)

        :param newdata: dict containing new data for prediction (needs the keys below, if None predicts on training data)
        :type newdata: dict
        :param f: (M,N) matrix of functions
        :param time: vector of time points
        :param y: truth if available
        :param smooth: smooth data if needed
        :param sparam: number of times to run filter
        """

        m = self.n_classes

        if newdata is not None:
            f = newdata["f"]
            n = f.shape[1]
            y = newdata["y"]
            if newdata["smooth"]:
                sparam = newdata["sparam"]
                f = fs.smooth_data(f, sparam)

            self.pca.project(f)
            a = self.pca.new_coef

            self.y_pred = np.zeros(n)
            for ii in range(0, n):
                for jj in range(0, m):
                    self.y_pred[ii, jj] = self.alpha[jj] + np.sum(
                        a[ii, :] * self.b[:, jj]
                    )

            if y is None:
                self.y_pred = rg.phi(self.y_pred.reshape((1, n * m)))
                self.y_pred = self.y_pred.reshape((n, m))
                self.y_labels = np.argmax(self.y_pred, axis=1)
                self.PC = np.nan
            else:
                self.y_pred = rg.phi(self.y_pred.reshape((1, n * m)))
                self.y_pred = self.y_pred.reshape((n, m))
                self.y_labels = np.argmax(self.y_pred, axis=1)
                self.PC = np.zeros(m)
                cls_set = np.arange(0, m)
                for ii in range(0, m):
                    cls_sub = np.setdiff1d(cls_set, ii)
                    TP = np.sum(y[self.y_labels == ii] == ii)
                    FP = np.sum(y[np.in1d(self.y_labels, cls_sub)] == ii)
                    TN = np.sum(
                        y[np.in1d(self.y_labels, cls_sub)]
                        == self.y_labels[np.in1d(self.y_labels, cls_sub)]
                    )
                    FN = np.sum(np.in1d(y[self.y_labels == ii], cls_sub))
                    self.PC[ii] = (TP + TN) / (TP + FP + FN + TN)

                self.PCo = np.sum(y == self.y_labels) / self.y_labels.shape[0]
        else:
            n = self.pca.coef.shape[0]
            self.y_pred = np.zeros((n, m))
            for ii in range(0, n):
                for jj in range(0, m):
                    self.y_pred[ii, jj] = self.alpha[jj] + np.sum(
                        self.pca.coef[ii, :] * self.b[:, jj]
                    )

            self.y_pred = rg.phi(self.y_pred.reshape((1, n * m)))
            self.y_pred = self.y_pred.reshape((n, m))
            self.y_labels = np.argmax(self.y_pred, axis=1)
            self.PC = np.zeros(m)
            cls_set = np.arange(0, m)
            for ii in range(0, m):
                cls_sub = np.setdiff1d(cls_set, ii)
                TP = np.sum(self.y[self.y_labels == ii] == ii)
                FP = np.sum(self.y[np.in1d(self.y_labels, cls_sub)] == ii)
                TN = np.sum(
                    self.y[np.in1d(self.y_labels, cls_sub)]
                    == self.y_labels[np.in1d(self.y_labels, cls_sub)]
                )
                FN = np.sum(np.in1d(y[self.y_labels == ii], cls_sub))
                self.PC[ii] = (TP + TN) / (TP + FP + FN + TN)

            self.PCo = np.sum(y == self.y_labels) / self.y_labels.shape[0]

        return
