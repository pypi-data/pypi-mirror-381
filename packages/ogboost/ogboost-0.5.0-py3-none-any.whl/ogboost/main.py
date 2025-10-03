"""
Gradient Boosting for Ordinal Regression

This module implements a gradient boosting framework for ordinal regression, 
allowing for custom link functions, sample weighting, and flexible early stopping criteria. 

Classes
-------
- LinkFunctions: A utility class providing common link functions (probit, logit, cloglog)
  and their derivatives/inverses for ordinal regression.
- GradientBoostingOrdinal: A gradient boosting model for ordinal regression.

Functions
---------
- concordance_index: Computes the concordance index (C-index) to evaluate the concordance 
  between predicted scores and true ordinal labels.

Features
--------
- Supports sample weighting for fit, scoring, and gradient computations.
- Allows customization of link functions (probit, logit, cloglog).
- Incorporates subsampling for stochastic gradient boosting.
- Provides staged prediction methods for both latent scores and class probabilities.
- Implements early stopping based on holdout loss.
- Fully compatible with scikit-learn's API for easy integration with existing pipelines.

Example Usage
-------------
```python
# Load wine quality data
from gbor.data import load_wine_quality
df_red, _ = load_wine_quality()

# prepare training data
X = df_red.drop('quality', axis=1)
y = df_red['quality']


# Initialize and train the model
from gbor.main import GradientBoostingOrdinal
model = GradientBoostingOrdinal(n_estimators=50, link_function='logit')
model.fit(X, y)

# Make predictions
pred_labels = model.predict(X)
pred_probs = model.predict_proba(X)
pred_latent = model.decision_function(X)
"""
from itertools import combinations
import warnings
import numpy as np
from scipy.stats import norm
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.tree import DecisionTreeRegressor
from sklearn.utils import check_array
from sklearn.base import clone
from sklearn.model_selection import train_test_split
from sklearn.utils.validation import check_is_fitted
from sklearn.utils.validation import validate_data

class LinkFunctions:
    """
    A collection of static methods for various link functions and 
    their derivatives used in statistical modeling.

    Supported Link Functions:
    - Probit
    - Logit
    - Complementary log-log (cloglog)
    Each link function includes its corresponding derivative and inverse function.
    """

    @staticmethod
    def probit(x):
        """
        Computes the probit link function for a given input.

        Parameters
        ----------
        x : float or array-like
            The input value(s).

        Returns
        -------
        float or ndarray
            The computed probit link value(s).
        """
        return norm.cdf(x)

    @staticmethod
    def probit_derivative(x):
        """
        Computes the derivative of the probit link function.

        Parameters
        ----------
        x : float or array-like
            The input value(s).

        Returns
        -------
        float or ndarray
            The derivative of the probit link function.
        """
        return norm.pdf(x)

    @staticmethod
    def probit_inverse(p):
        """
        Computes the inverse of the probit link function.

        Parameters
        ----------
        p : float or array-like
            The probability value(s).

        Returns
        -------
        float or ndarray
            The inverse probit value(s).
        """
        return norm.ppf(p)

    @staticmethod
    def logit(x):
        """
        Computes the logit link function for a given input.

        Parameters
        ----------
        x : float or array-like
            The input value(s).

        Returns
        -------
        float or ndarray
            The computed logit link value(s).
        """
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def logit_derivative(x):
        """
        Computes the derivative of the logit link function.

        Parameters
        ----------
        x : float or array-like
            The input value(s).

        Returns
        -------
        float or ndarray
            The derivative of the logit link function.
        """
        sig = 1 / (1 + np.exp(-x))
        return sig * (1 - sig)

    @staticmethod
    def logit_inverse(p):
        """
        Computes the inverse of the logit link function.

        Parameters
        ----------
        p : float or array-like
            The probability value(s).

        Returns
        -------
        float or ndarray
            The inverse logit value(s).
        """
        return np.log(p / (1 - p))

    @staticmethod
    def cloglog(x):
        """
        Computes the complementary log-log (cloglog) link function.

        Parameters
        ----------
        x : float or array-like
            The input value(s).

        Returns
        -------
        float or ndarray
            The computed cloglog link value(s).
        """
        return 1 - np.exp(-np.exp(x))

    @staticmethod
    def cloglog_derivative(x):
        """
        Computes the derivative of the cloglog link function.

        Parameters
        ----------
        x : float or array-like
            The input value(s).

        Returns
        -------
        float or ndarray
            The derivative of the cloglog link function.
        """
        return np.exp(x - np.exp(x))

    @staticmethod
    def cloglog_inverse(p):
        """
        Computes the inverse of the complementary log-log (cloglog) link function.

        Parameters
        ----------
        p : float or array-like
            The probability value(s).

        Returns
        -------
        float or ndarray
            The inverse cloglog value(s).
        """
        return np.log(-np.log(1 - p))

class GradientBoostingOrdinal(ClassifierMixin, BaseEstimator):
    """
    Gradient Boosting for Ordinal Regression

    This class implements a gradient boosting framework for ordinal regression,
    which optimizes an objective function designed for ordered target variables.
    It supports custom link functions, sample weighting, early stopping, and
    flexible subsampling for stochastic gradient boosting.

    Parameters
    ----------
    base_learner : object, default=DecisionTreeRegressor(max_depth=3)
        The weak learner to be used for boosting. Must implement `fit` and `predict`.

    n_estimators : int, default=100
        The maximum number of boosting iterations.

    learning_rate : float, default=0.1
        The step size for updating latent scores during boosting iterations.

    learning_rate_thresh : float, default=0.001
        The initial step size for updating thresholds.

    validation_fraction : float, default=0.1
        Fraction of data to be used for validation when early stopping is enabled.

    n_iter_no_change : int or None, default=None
        Number of iterations with no improvement in validation loss to trigger
        early stopping. If None, early stopping is not used.

    tol : float, default=1e-4
        Tolerance for improvement in validation loss to determine early stopping.

    validation_stratify : bool, default=True
        Whether to stratify the validation split by target values when performing
        early stopping.

    n_class : int or None, default=None
        The number of ordinal classes. If None, inferred automatically from the
        training data. Specify this explicitly when some subsets of data (e.g.,
        during cross-validation) may not contain all levels of the target variable.

    link_function : {'probit', 'logit', 'cloglog'}, default='probit'
        The link function to be used for probability transformations.

    subsample : float, default=1.0
        The fraction of samples to be used in each boosting iteration. Must be
        within the range (0, 1]. Values less than 1 enable stochastic gradient
        boosting.

    verbose : int, default=0
        Controls the verbosity of logging during training:
        - 0: No output.
        - 1: Logs progress at regular intervals (e.g., every 10% of n_estimators).
        - 2: Logs detailed progress for each iteration, including training and
             validation loss.

    random_state : int, RandomState instance, or None, default=None
        Controls the random number generator used for subsampling, splitting, and
        base learner randomization. Ensures reproducibility when set.

    Attributes
    ----------
    classes_ : ndarray of shape (n_classes,)
        The class labels inferred or explicitly set during training.

    n_estimators_ : int
        The actual number of boosting iterations performed.

    _init : dict
        Initial model state, including:
        - `g` : array of shape (n_samples,)
            Initial latent scores for the target variable.
        - `theta` : array of shape (n_classes - 1,)
            Initial thresholds separating ordinal categories.
        - `loss` : float
            Initial value of the loss function.

    _final : dict
        Final model state after training, including:
        - `g` : array of shape (n_samples,)
            Final latent scores for the target variable.
        - `theta` : array of shape (n_classes - 1,)
            Final thresholds separating ordinal categories.
        - `loss` : float
            Final value of the loss function.

    _path : dict
        Tracks the evolution of model parameters during training:
        - `g` : array of shape (n_estimators + 1, n_samples)
            Latent scores at each iteration, including the initial state.
        - `theta` : array of shape (n_estimators + 1, n_classes - 1)
            Thresholds at each iteration, including the initial state.
        - `loss` : array of shape (n_estimators + 1,)
            Training loss at each iteration, including the initial state.
        - `loss_diff` : tuple of arrays
            Differences in loss values for g and theta updates at each iteration.
        - `learner` : list of base learners, length n_estimators.
            Weak learners fitted during training.
        - `intercept` : array of shape (n_estimators,)
            Intercept values for each base learner.
        - `learning_rate_thresh` : array of shape (n_estimators,)
            Learning rate for threshold updates at each iteration.
        - `loss_holdout` : array of shape (n_estimators + 1,), optional
            Validation loss at each iteration (including the initial state), 
            if early stopping is enabled.

    Requirements
    ------------
    y : array-like of shape (n_samples,)
        - Must contain ordinal labels as integers starting from 0.
        - Labels must be non-negative (minimum value is 0).
        - Labels must have no gaps in the sequence (e.g., `[0, 1, 2]` is valid, but
          `[0, 2]` is not).
        - If `n_class` is specified, labels must be within the range [0, n_class-1], but 
          there can be gaps in the sequence.

    Notes
    -----
    The model optimizes a loss function designed for ordinal regression, where:
    - `g` (Latent Scores): Continuous values representing the raw model predictions.
    - `theta` (Thresholds): Values separating ordinal categories, derived from the
      specified link function.
    The loss is computed as a function of `g` and `theta`, transformed by the link
    function.

    The `n_class` parameter is particularly useful in scenarios like cross-validation,
    where subsets of data may not contain all levels of the target variable. By
    explicitly setting `n_class`, you can ensure consistency in the model's
    behavior.

    Examples
    --------
    Basic Usage:
    >>> from gbor.main import GradientBoostingOrdinal
    >>> model = GradientBoostingOrdinal(n_estimators=50, link_function='logit')
    >>> model.fit(X, y)
    >>> preds = model.predict(X)

    Early Stopping:
    >>> model = GradientBoostingOrdinal(
    ...     n_estimators=100, n_iter_no_change=10, validation_fraction=0.2
    ... )
    >>> model.fit(X, y)

    Staged Predictions:
    >>> for stage_probs in model.staged_predict_proba(X):
    ...     print(stage_probs[:5])

    Custom Base Learner:
    >>> from sklearn.ensemble import RandomForestRegressor
    >>> model = GradientBoostingOrdinal(base_learner=RandomForestRegressor(n_estimators=10))
    >>> model.fit(X, y)
    """

    def _get_random_state(self):
        """
        Retrieve or create the RandomState instance.

        Returns
        -------
        np.random.RandomState
            Random number generator instance.
        """
        if self.random_state is None:
            return np.random.mtrand._rand  # Default global RNG
        if isinstance(self.random_state, (int, np.integer)):
            return np.random.RandomState(self.random_state)
        if isinstance(self.random_state, np.random.RandomState):
            return self.random_state
        raise ValueError("random_state must be None, an int, or a RandomState instance.")

    
    def __init__(
        self,
        base_learner=DecisionTreeRegressor(max_depth=3),
        n_estimators=100,
        learning_rate=1e-1,
        learning_rate_thresh=1e-3,
        validation_fraction=0.1,
        n_iter_no_change=None,
        tol=1e-4,
        validation_stratify=True,
        n_class=None,
        link_function='probit',
        subsample=1.0,
        verbose=0,
        random_state=None
    ):
        self.base_learner = base_learner
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.learning_rate_thresh = learning_rate_thresh
        self.validation_fraction = validation_fraction
        self.n_iter_no_change = n_iter_no_change
        self.tol = tol
        self.validation_stratify = validation_stratify
        self.n_class = n_class
        self.link_function = link_function
        self.subsample = subsample
        self.verbose = verbose
        self.random_state = random_state

    def fit(self, X, y, sample_weight=None):
        """
        Fit the GradientBoostingOrdinal model.

        This method fits the model to the training data by iteratively optimizing
        the latent scores and thresholds using gradient boosting.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input feature matrix.
        y : array-like of shape (n_samples,)
            The target variable with ordinal labels.
        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights for each observation. If None, all samples are treated equally.

        Returns
        -------
        self : object
            The fitted model.

        Notes
        -----
        - If `n_iter_no_change` is set, a portion of the data will be used as a
          validation set to monitor early stopping.
        - If `subsample` is less than 1.0, the model performs stochastic gradient boosting.
        """
        
        # set up base learner
        base_learner = clone(self.base_learner)
        if hasattr(base_learner, 'random_state'):
            base_learner.set_params(random_state=self.random_state)
        
        # validate sample weights
        if sample_weight is None:
            sample_weight = np.ones_like(y, dtype=float)
        else:
            sample_weight = np.asarray(sample_weight)
            if sample_weight.shape[0] != y.shape[0]:
                raise ValueError("sample_weight must have the same length as y")
            if np.any(sample_weight < 0):
                raise ValueError("sample_weight cannot contain negative values")
            if np.sum(sample_weight) <= 0:
                raise ValueError("sample_weight must have positive sum")
        
        # validate X and y
        X, y = validate_data(self, X, y)

        # validate link function
        if self.link_function not in ['probit', 'logit', 'cloglog']:
            raise ValueError("Invalid link function, must be 'probit', 'logit', or 'cloglog'")
        
        # validate subsample
        if not 0 < self.subsample <= 1:
            raise ValueError("subsample must be in the range (0, 1]")


        # Possibly split X_holdout, y_holdout if needed
        if self.n_iter_no_change:
            X, X_holdout, y, y_holdout, sample_weight, sample_weight_holdout = train_test_split(
                X, y, sample_weight,
                test_size=self.validation_fraction,
                stratify=y if self.validation_stratify else None,
                random_state=self._get_random_state()
            )

        # Validate ordinal data, possibly sets self._n_class
        ylist = self._validate_ordinal(y)
        self.classes_ = np.arange(self._n_class)

        # Initialize g and theta
        # NOTE: currently, initia
        g_init, theta_init = self._initialize(
            y, n_class=self._n_class, laplace_smoothing=True
        )
        loss_init = self._loss_function(y, g_init, theta_init, sample_weight=sample_weight)

        g, theta, loss = g_init, theta_init, loss_init
        loss_all = []
        learner_all = []
        intercept_all = []
        g_all = []
        theta_all = []

        if self.n_iter_no_change:
            g_init_holdout = self._initialize_g(y_holdout)
            loss_holdout = self._loss_function(
                y_holdout, g_init_holdout, 
                theta_init, sample_weight=sample_weight_holdout
            )
            loss_all_holdout = [loss_holdout]
            g_holdout = g_init_holdout.copy()

        loss_all.append(loss)
        g_all.append(g.copy())
        theta_all.append(theta.copy())

        no_change = False
        lr_theta = self.learning_rate_thresh
        lr_theta_all = [lr_theta]

        if self.n_iter_no_change:
            loss_history = np.full(self.n_iter_no_change, np.inf)

        for p in range(self.n_estimators):

            if self.subsample < 1.0:
                n_samples = X.shape[0]
                sample_indices = self._get_random_state().choice(
                    np.arange(n_samples),
                    size=int(n_samples * self.subsample),
                    replace=False,
                    p=sample_weight / np.sum(sample_weight) if sample_weight is not None else None
                )
                X_sub, y_sub = X[sample_indices], y[sample_indices]
                sw_sub = sample_weight[sample_indices] if sample_weight is not None else None
            else:
                X_sub, y_sub, sw_sub = X, y, sample_weight
                sample_indices = np.arange(X.shape[0])


            # Compute derivative wrt g
            dg = self._derivative_g(y_sub, theta, g[sample_indices], sample_weight=sw_sub)
            # Fit a weak learner on -dg
            weak_learner, intercept = GradientBoostingOrdinal._fit_weak_learner(
                X_sub, -dg, clone(base_learner)
            )
            # Update g
            h_full = weak_learner.predict(X) + intercept
            g = GradientBoostingOrdinal._update_g(g, h_full, lr=self.learning_rate)

            # Update loss
            loss = self._loss_function(y, g, theta, sample_weight=sample_weight)
            loss_all.append(loss)

            # Compute derivative wrt theta
            dtheta = self._derivative_threshold(X, ylist, theta, g, sample_weight=sample_weight)
            # Update theta (with auto-tuned learning rate)
            theta, lr_theta = self._update_thresh(
                theta, dtheta, lr_theta, y, g, frac=0.5, sample_weight=sample_weight
            )

            # Update loss
            loss = self._loss_function(y, g, theta, sample_weight=sample_weight)
            loss_all.append(loss)

            learner_all.append(weak_learner)
            intercept_all.append(intercept)
            g_all.append(g.copy())
            theta_all.append(theta.copy())
            lr_theta_all.append(lr_theta)

            # Check early stopping if n_iter_no_change is set
            if self.n_iter_no_change:
                h_holdout = weak_learner.predict(X_holdout) + intercept
                g_holdout = GradientBoostingOrdinal._update_g(
                    g_holdout, h_holdout, lr=self.learning_rate
                )
                loss_holdout = self._loss_function(
                    y_holdout, g_holdout, theta, sample_weight=sample_weight_holdout
                )
                loss_all_holdout.append(loss_holdout)

                # Verbose logging
                if self.verbose > 0:
                    if self.verbose == 1:
                        # Print at regular intervals (e.g., every 10% of n_estimators)
                        if p % max(1, self.n_estimators // 10) == 0:
                            print(f"Iteration {p}/{self.n_estimators}, Loss: {loss:.4f}, Holdout Loss: {loss_holdout:.4f}")
                    elif self.verbose > 1:
                        # Print every iteration
                        print(f"Iteration {p}, Loss: {loss:.4f}, Holdout Loss: {loss_holdout:.4f}")
                
                if np.any(loss_holdout + self.tol < loss_history):
                    loss_history = np.roll(loss_history, -1)
                    loss_history[-1] = loss_holdout
                else:
                    no_change = True
                    if self.verbose > 0:
                        print(f"Stopping early after {p+1} iterations due to no significant improvement.")
                    break

            else:
                if self.verbose > 0:
                    if self.verbose == 1:
                        # Print at regular intervals (e.g., every 10% of n_estimators)
                        if p % max(1, self.n_estimators // 10) == 0:
                            print(f"Iteration {p}/{self.n_estimators}, Loss: {loss:.4f}")
                    elif self.verbose > 1:
                        # Print every iteration
                        print(f"Iteration {p}, Loss: {loss:.4f}")

        self.n_estimators_ = p + 1 if no_change else self.n_estimators
        self._init = {'g': g_init, 'theta': theta_init, 'loss': loss_init}
        self._final = {'g': g, 'theta': theta, 'loss': loss_all[-1]}
        loss_all = np.array(loss_all)
        self._path = {
            'g': np.array(g_all),
            'theta': np.array(theta_all),
            'loss': loss_all[::2],
            'loss_diff': self._check_loss_change(loss_all),
            'learner': learner_all,
            'intercept': np.array(intercept_all),
            'learning_rate_thresh': np.array(lr_theta_all)
        }
        if self.n_iter_no_change:
            self._path['loss_holdout'] = np.array(loss_all_holdout)
        
        return self

    #def predict_latent(self, X, path=False):
    #    if path:
    #        return list(self.staged_decision_function(X))
    #    else:
    #        return self.decision_function(X)

    def decision_function(self, X):
        """
        Compute latent scores for the input data.

        The latent scores are continuous values representing the model's predictions
        before applying thresholds to compute class probabilities or labels.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input feature matrix.

        Returns
        -------
        latent : ndarray of shape (n_samples,)
            Latent scores for each sample.
        """
        check_is_fitted(self)
        X = check_array(X)

        # Compute raw predictions from all estimators
        per_iter_raw = np.array([
            learner.predict(X) + self._path['intercept'][p]
            for p, learner in enumerate(self._path['learner'])
        ])

        g_init = self._initialize_g(np.zeros(X.shape[0]))

        # Return final latent predictions
        final_raw = np.sum(per_iter_raw[:self.n_estimators_], axis=0) * self.learning_rate + g_init
        return final_raw

    def staged_decision_function(self, X):
        """
        Yield the continuous latent scores for each boosting iteration.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Feature matrix for which to compute the latent predictions.

        Yields
        ------
        latent : ndarray of shape (n_samples,)
            Latent scores computed after each boosting iteration.
        """
        check_is_fitted(self)
        X = check_array(X)

        # Compute raw predictions from all estimators
        per_iter_raw = np.array([
            learner.predict(X) + self._path['intercept'][p]
            for p, learner in enumerate(self._path['learner'])
        ])

        g_init = self._initialize_g(np.zeros(X.shape[0]))
        
        # Yield cumulative latent scores for each iteration
        cum_preds = np.cumsum(per_iter_raw, axis=0) * self.learning_rate + g_init
        for i in range(cum_preds.shape[0]):
            yield cum_preds[i, :]

    def predict_proba(self, X):
        """
        Predict class probabilities for the given input data.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The input feature matrix.

        Returns
        -------
        probs : ndarray of shape (n_samples, n_classes)
            Predicted probabilities for each class.
        """
        check_is_fitted(self)

        # 1) Get latent values from the decision function
        latent_values = self.decision_function(X)

        # 2) Convert latent values to probabilities
        final_theta = self._path['theta'][-1]
        return self._probabilities(latent_values, final_theta, y=None)

    def staged_predict_proba(self, X):
        """
        Predict class probabilities at each stage of boosting.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)

        Returns
        -------
        generator
            A generator yielding class probabilities for each boosting stage,
            where each element is an ndarray of shape (n_samples, n_classes).
        """
        check_is_fitted(self)

        # Per-iteration latent predictions
        staged_latent = self.staged_decision_function(X)
        
        # Generator to iterate through stage-wise decision functions
        for i, g_iter in enumerate(staged_latent):
            # Use the appropriate threshold index for the stage
            theta_idx = min(i + 1, len(self._path['theta']) - 1)
            yield self._probabilities(g_iter, self._path['theta'][theta_idx], y=None)
    
    def predict(self, X):
        """
        Predict class labels for X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)

        Returns
        -------
        labels : ndarray of shape (n_samples,)
            Predicted class labels for each sample.
        """
        check_is_fitted(self)

        # 1) Get final probabilities
        probs = self.predict_proba(X)

        # 2) Convert probabilities to labels
        return self._class_labels(probs)

    def staged_predict(self, X):
        """
        Predict class labels at each stage of boosting.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)

        Returns
        -------
        generator
            A generator yielding class label arrays for each boosting stage,
            where each element is an ndarray of shape (n_samples,).
        """
        check_is_fitted(self)

        # Generator to iterate through stage-wise probabilities
        for stage_probs in self.staged_predict_proba(X):
            yield self._class_labels(stage_probs)

    # --------------------------------------------------------------------------
    # Other internal methods remain as is
    # --------------------------------------------------------------------------
    @staticmethod
    def _class_labels(probs, axis=1):
        return np.argmax(probs, axis=axis)

    def _probabilities(self, g, theta, y=None):
        F = getattr(LinkFunctions, self.link_function)
        probs = np.array([np.diff(F(GradientBoostingOrdinal._pad_thresholds(theta - x))) for x in g])
        # (Optional) Handle log-likelihood if needed
        if y is None:
            return probs
        loglike = sum([np.log(probs[n, yn]) for n, yn in enumerate(y)])
        return probs, loglike
    
    @staticmethod
    def _check_loss_change(loss):
        x = np.diff(loss)
        return (x[::2], x[1::2]) # (g, theta)
    
    def _validate_ordinal(self, arr):
    
        if not isinstance(arr, np.ndarray):
            raise ValueError("Input must be a numpy array")
        if arr.dtype.kind not in {'i', 'u'}:
            raise ValueError("Input array must contain integers")
        
        unique_values = np.unique(arr) # we rely on numpy.unique returning a sorted array
        min_value, max_value = unique_values[0], unique_values[-1]
    
        if min_value < 0:
            raise ValueError("Minimum of arr cannot be less than 0")
    
        if not self.n_class:
            check_gap = True
            self._n_class = max_value + 1
        else:
            check_gap = False
            self._n_class = self.n_class
        
        if max_value >= self._n_class:
            raise ValueError("Maximum of arr cannot be more than n_class-1")
        
        expected_values = np.arange(self._n_class)
        
        if check_gap:
            if not np.array_equal(expected_values, unique_values):
                raise ValueError("Unique values in arr have gaps")
    
        return [np.where(arr == m) for m in expected_values]
        
    def _initialize(self, y, n_class=None, laplace_smoothing=False):
        return (
            GradientBoostingOrdinal._initialize_g(y), 
            self._initialize_thresholds(y, n_class=n_class, laplace_smoothing=laplace_smoothing)
        )
    
    @staticmethod
    def _initialize_g(y):
        return np.zeros(len(y))
    
    def _initialize_thresholds(self, y, n_class=None, laplace_smoothing=False):
        """
        Initialize the threshold vector theta based on class probabilities and 
        the inverse link function.

        Parameters
        ----------
        y : array-like of shape (n_samples,)
            Target values.
        n_class : int, optional (default=None)
            Number of classes. If None, inferred from y.
        laplace_smoothing : bool, default=False
            Whether to apply Laplace smoothing to class probabilities.

        Returns
        -------
        theta : ndarray of shape (n_classes - 1,)
            Initialized threshold vector.
        """
        # Calculate the initial threshold vector
        n_samples = len(y)
        
        if n_class is None:
            n_class = np.max(y) + 1
        else:
            if np.max(y) + 1 > n_class:
                raise ValueError('Class count cannot be smaller than count of unique values in y')
        
        # Calculate class probabilities with optional Laplace smoothing
        P = (
            np.array([np.sum(y == i) + laplace_smoothing for i in range(n_class)]) 
            / (n_samples + laplace_smoothing * n_class)
        )
        
        # Compute cumulative probabilities excluding the last class
        cumulative_P = np.cumsum(P[:-1])
        
        # Retrieve the inverse link function based on the specified link function
        inverse_link_func = getattr(LinkFunctions, f"{self.link_function}_inverse")
        
        # Apply the inverse link function to the cumulative probabilities to obtain initial thresholds
        theta = inverse_link_func(cumulative_P)
        
        return theta

    @staticmethod
    def _pad_thresholds(theta):
        return np.insert(theta, [0, theta.size], [-np.inf, np.inf])
    
    def _derivative_threshold(self, X, ylist, thresh, g, return_mean=False, sample_weight=None):
        # Access the link function and its derivative
        link_func = getattr(LinkFunctions, self.link_function)
        link_derivative = getattr(LinkFunctions, f"{self.link_function}_derivative")
        
        thresh_padded = self._pad_thresholds(thresh)
        M = len(thresh)
        ret = []
        for m in range(M):
            S_m = ylist[m]
            S_mp1 = ylist[m+1]
            
            # Apply the link function and its derivative
            z_m = thresh_padded[m+1] - g[S_m]
            z_mp1 = thresh_padded[m+1] - g[S_mp1]
            
            # Compute terms involving the link function derivative
            v1_vec = link_derivative(z_m) / (link_func(z_m) - link_func(thresh_padded[m] - g[S_m]))
            v2_vec = link_derivative(z_mp1) / (link_func(thresh_padded[m+2] - g[S_mp1]) - link_func(z_mp1))
            
            if sample_weight is not None:
                v1_vec *= sample_weight[S_m]
                v2_vec *= sample_weight[S_mp1]
            
            v1 = np.sum(v1_vec)
            v2 = np.sum(v2_vec)
            tmp = -v1 + v2
            if return_mean:
                tmp = tmp / X.shape[0]
            ret.append(tmp)
        
        return np.array(ret)
    
    def _derivative_g(self, y, thresh, g, sample_weight=None):
        """
        Compute the derivative of the loss with respect to the latent variable g.

        Parameters
        ----------
        y : array-like of shape (n_samples,)
            True target values.
        thresh : array-like of shape (n_classes - 1,)
            Thresholds separating the ordinal categories.
        g : array-like of shape (n_samples,)
            Predicted latent scores.
        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.

        Returns
        -------
        derivatives : ndarray of shape (n_samples,)
            Derivatives with respect to g.
        """
        # Access the link function and its derivative
        F_prime = getattr(LinkFunctions, f"{self.link_function}_derivative")
        F = getattr(LinkFunctions, self.link_function)  # For consistency

        # Pad the thresholds
        thresh_padded = GradientBoostingOrdinal._pad_thresholds(thresh)

        # Compute numerator and denominator
        num = F_prime(thresh_padded[y + 1] - g) - F_prime(thresh_padded[y] - g)
        denom = F(thresh_padded[y + 1] - g) - F(thresh_padded[y] - g)

        # Compute derivatives
        derivatives = num / denom

        # Apply sample weights if provided
        if sample_weight is not None:
            derivatives *= sample_weight

        return derivatives

    @staticmethod
    def _fit_weak_learner(X, pseudo_resids, learner):
        learner.fit(X, pseudo_resids)
        pred = learner.predict(X)
        intercept = -np.mean(pred) # we could also perform intercept adjustment in _update_g but mathematically the effect is the same
        return (learner, intercept)
    
    # replace with more sophisticated version that performs line search
    @staticmethod
    def _update_g(g, h, lr = 1e-1):
        return g + lr * h
    
    # this can be fused with _probabilities, though this is likely more efficient is the goal is only loss and not the prob matrix
    def _loss_function(self, y, g, theta, sample_weight=None):
        """
        Compute the loss for the given predictions and thresholds.

        Parameters
        ----------
        y : array-like of shape (n_samples,)
            True target values.
        g : array-like of shape (n_samples,)
            Predicted latent scores.
        theta : array-like of shape (n_classes - 1,)
            Thresholds separating ordinal categories.
        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.

        Returns
        -------
        loss : float
            The computed loss value.
        """
        F = getattr(LinkFunctions, self.link_function)
        theta_padded = GradientBoostingOrdinal._pad_thresholds(theta)
        log_probs = np.log(F(theta_padded[y + 1] - g) - F(theta_padded[y] - g))
        if sample_weight is not None:
            return -np.mean(sample_weight * log_probs)
        return -np.mean(log_probs)
    
    def _update_thresh(self, thresh, dthresh, lr, y, g, frac = 0.5, sample_weight=None):
        this_accept = self._try_thresh(thresh, thresh - lr * dthresh, y, g, sample_weight=sample_weight)
        if this_accept:
            # keep doubling till reject
            lr_proposed = lr
            while this_accept:
                lr = lr_proposed
                lr_proposed = lr / frac
                this_accept = self._try_thresh(thresh - lr * dthresh, thresh - lr_proposed * dthresh, y, g, sample_weight=sample_weight)
        else:
            # keep halving till accept
            while not this_accept:
                lr = lr * frac
                this_accept = self._try_thresh(thresh, thresh - lr * dthresh, y, g, sample_weight=sample_weight)

        return (thresh - lr * dthresh, lr)

    def _try_thresh(self, thresh_i, thresh_f, y, g, sample_weight=None):
        #try:
        with warnings.catch_warnings(record=True) as w:
            _ = self._loss_function(y, g, thresh_f, sample_weight=sample_weight)
        if w:
            return False
        #except:
        #    return False
        
        return (self._loss_function(y, g, thresh_f, sample_weight=sample_weight) < self._loss_function(y, g, thresh_i, sample_weight=sample_weight)) and (np.all(np.diff(thresh_f) > 0))
    
    # score function using concordance index
    def score(self, X, y, sample_weight=None, pred_type='labels'):
        """
        Compute a performance score for the model.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Input features.
        y : array-like of shape (n_samples,)
            True target values.
        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights.
        pred_type : {'labels', 'latent'}, default='labels'
            Type of prediction to use for scoring.
            - 'labels': Use class labels.
            - 'latent': Use continuous latent scores.
            
        Returns
        -------
        score : float
            The computed score.
        """
        # Get predictions based on pred_type
        if pred_type == 'labels':
            y_pred = self.predict(X)
        elif pred_type == 'latent':
            y_pred = self.decision_function(X)
        else:
            raise ValueError("Invalid pred_type, must be 'labels' or 'latent'")
        
        # Compute concordance index, using sample weights if provided
        return concordance_index(y, y_pred, sample_weight=sample_weight)

def concordance_index(y_true, y_pred, sample_weight=None):
    """
    Compute the concordance index (C-index) for ordinal predictions, optionally
    weighted by sample weights.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True ordinal labels.
        
    y_pred : array-like of shape (n_samples,)
        Predicted scores or continuous outputs from the model.
        
    sample_weight : array-like of shape (n_samples,), default=None
        Weights for each sample. If None, all samples are equally weighted. Note that
        weights for each member of a pair of samples are multiplied when computing the
        contribution of the pair to the concordance index.

    Returns
    -------
    float
        Concordance index, ranging from 0 to 1. A higher value indicates better concordance.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    if sample_weight is None:
        sample_weight = np.ones_like(y_true, dtype=float)
    else:
        sample_weight = np.asarray(sample_weight)
        if sample_weight.shape[0] != y_true.shape[0]:
            raise ValueError("sample_weight must have the same length as y_true")
        if np.any(sample_weight < 0):
            raise ValueError("sample_weight cannot contain negative values")
        if np.sum(sample_weight) <= 0:
            raise ValueError("sample_weight must have positive sum")
    
    # Check that the input sizes match
    if y_true.shape[0] != y_pred.shape[0]:
        raise ValueError("y_true and y_pred must have the same length")
    
    # Pairwise comparisons
    pairs = list(combinations(range(len(y_true)), 2))
    concordant, permissible = 0.0, 0.0
    
    for i, j in pairs:
        if y_true[i] != y_true[j]:  # Skip ties in true labels
            weight = sample_weight[i] * sample_weight[j]  # Weight for the pair
            permissible += weight
            if (y_true[i] < y_true[j] and y_pred[i] < y_pred[j]) or \
               (y_true[i] > y_true[j] and y_pred[i] > y_pred[j]):
                concordant += weight
            elif y_pred[i] == y_pred[j]:  # Handle ties in predictions
                concordant += 0.5 * weight

    return concordant / permissible if permissible > 0 else 0.0
