# Ordinal Gradient Boosting (`OGBoost`)

## Overview

`OGBoost` is a scikit-learn-compatible, Python package for gradient boosting tailored to ordinal regression problems. It does so by alternating between:
1. Fitting a Machine Learning (ML) regression model - such as a decision tree - to predict a latent score that specifies the mean of a probability density function (PDF), and 
1. Fitting a set of thresholds that generate discrete outcomes from the PDF.

In other words, `OGBoost` implements coordinate-descent optimization that combines functional gradient descent - for updating the regression function - with ordinary gradient descent - for updating the threshold vector.

The main class of the package, `GradientBoostingOrdinal`, is designed to have the same look and feel as `scikit-learn`'s `GradientBoostingClassifier`. It includes many of the same features such as custom link functions, sample weighting, early stopping using a validation set, and staged predictions.

There are, however, important differences as well.

## Unique Features of `OGBoost`

### Latent-Score Prediction

The `decision_function` method of the `GradientBoostingOrdinal` behaves differently from `scikit-learn`'s classifiers. Assuming the target variable has `K` distinct classes, a nominal classifier's decision function would return `K` values for each sample. On the other hand, `decision_function` in `ogboost` would return the latent score for each sample, which is a single value. This latent score can be considered a high-resolution alternative to class labels, and thus may have superior ranking performance.

### Early Stopping using Cross-Validation (CV)

In addition to using a single validation set for early stopping, similar to `GradientBoostingClassifier`, `ogboost` implements early stopping using CV, which means the entire data is used for calculating out-of-sample performance. This can improve the robustness of early-stopping, especially for small and/or imbalanced datasets.

### Heterogeneous Ensemble

While most gradient-boosting software packages exclusively use decision trees with a predetermined set of hyperparameters as the base learner in all boosting iterations, `ogboost` offers significantly more flexibility.

1. Users can pass in a `base_learner` parameter to the class initializer to override the default choice of a `DecisionTreeRegressor`. This can be any scikit-learn regression algorithm such as a feed-forward neural network (`MLPRegressor`), or a K-nearest-neighbor regressor (`KNeighborsRegressor`), etc.
1. Rather than a single base learner, users can specify a list (or a generator) of base learners, which will be drawn from in that order in each boosting iteration. This amounts to creating a *heterogeneous* ensemble as opposed to a *homogeneous* ensemble.

## Installation
```bash
pip install ogboost
```
To access `StatsModelsOrderedModel`, which is a wrapper for the `OrderedModel` class from the `statsmodels` package to make it compatible with `scikit-learn`, please run:
```bash
pip install ogboost[param]
```

## Package Vignette

For a more detailed introduction to `OGBoost`, including the underlying math, see the [package vignette](https://arxiv.org/abs/2502.13456), available on arXiv.

## Quick Start
### Load the Wine Quality Dataset
The package includes a utility to load the wine quality dataset (red and white) from the UCI repository. Note that `load_wine_quality` shifts the target variable (`quality`) to start from `0`. (This is required by the `GradientBoostingOrdinal` class.)

```python
from ogboost import load_wine_quality
X, y, _, _ = load_wine_quality(return_X_y=True)
```

### Training, Prediction and Evaluation
Latent scores perform better on discrminative tasks vs. class labels as they contain more information due to higher resolution:
```python
from ogboost import GradientBoostingOrdinal

## training ##
model = GradientBoostingOrdinal(n_estimators=100, link_function='logit', verbose=1)
model.fit(X, y)

## prediction ##
# class labels
predicted_labels = model.predict(X)
# class probabilities
predicted_probabilities = model.predict_proba(X)
# latent score
predicted_latent = model.decision_function(X)

# evaluation
concordance_latent = model.score(X, y) # concordance using latent scores
concordance_label = model.score(X, y, pred_type = 'labels') # concordance using class labels
print(f"Concordance - class labels: {concordance_label:.3f}")
print(f"Concordance - latent scores: {concordance_latent:.3f}")
```

### Early-Stopping using Cross-Validation
Using cross-validation for early stopping can produce more robust results compared to a single holdout set, especially for small and/or imbalanced datasets:
```python
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
import time

n_splits = 10
n_repeats = 10
kf = RepeatedKFold(n_splits=n_splits, n_repeats=n_repeats)

# early-stopping using a simple holdout set
model_earlystop_simple = GradientBoostingOrdinal(n_iter_no_change=10, validation_fraction=0.2)
start = time.time()
c_index_simple = cross_val_score(model_earlystop_simple, X, y, cv=kf, n_jobs=-1)
end = time.time()
print(f'Simple early stopping: {c_index_simple.mean():.3f} ({end - start:.1f} seconds)')

# early-stopping using cross-validation
model_earlystop_cv = GradientBoostingOrdinal(n_iter_no_change=10, cv_early_stopping_splits=5)
start = time.time()
c_index_cv = cross_val_score(model_earlystop_cv, X, y, cv=kf, n_jobs=-1)
end = time.time()
print(f'CV early stopping: {c_index_cv.mean():.3f} ({end - start:.1f} seconds)')
```

### Heterogeneous Ensemble

Rather than a single base learner, users can supply a heterogeneous list of base learners to ```GradientBoostingOrdinal```. The utility function ```generate_heterogeneous_learners``` can be used to easily generate random samples from hyperparameter spaces of one or more base learners:
```python
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from ogboost import generate_heterogeneous_learners

# Number of samples to generate
n_samples = 100

max_depth_choices = [3, 6, 9, None]
max_leaf_nodes_choices = [10, 20, 30, None]

dt_overrides = {
    "max_depth": lambda rng: rng.choice(max_depth_choices),
    "max_leaf_nodes": lambda rng: rng.choice(max_leaf_nodes_choices)
}

# Create list of DecisionTreeRegressor models
random_learners = generate_heterogeneous_learners(
    [DecisionTreeRegressor()], 
    [dt_overrides], 
    total_samples=n_samples
)
```
Such heterogenous boosting ensembles can be a more efficient alternative to hyperparameter tuning (e.g., via grid search):
```python
model_heter = GradientBoostingOrdinal(
    base_learner=random_learners,
    n_estimators=n_samples
)
cv_heter = cross_val_score(model_heter, X, y, cv=kf, n_jobs=-1)
print(f'average cv score of heterogeneous ensemble: {np.mean(cv_heter):.3f}')
```

### Parametric Ordinal Regression
The `StatsModelsOrderedModel` is a `scikit-learn` wrapper for the `OrderedModel` class of the `statsmodels` package:
```python
from ogboost import StatsModelsOrderedModel

cv_param = cross_val_score(StatsModelsOrderedModel(), X, y, cv=kf, n_jobs=-1)
print(f'average cv score of parametric model: {np.mean(cv_param):.3f}')
```
This model can be useful for benchmarking against ML models, or as part of an ensemble alongside them.

## License
This package is licensed under the [MIT License](./LICENSE).

## Release Notes

### 0.8.1

- Fixed numerical overflow warnings in logit link function by replacing manual `np.exp()` implementation with `scipy.special.expit()`, which provides better numerical stability for extreme values.

### 0.8.0

- Improved numerical stability across core methods by adding probability clipping and safeguards against division by zero and log of zero.
Introduced stratified cross-validation early stopping, with smart fallback to regular KFold and enhanced warning handling.
- Added robust line search safeguards to prevent infinite loops and improve error handling, especially for unstable base learners.
- Expanded testing infrastructure with a new module for CV stratification and improved handling of optional dependencies.
- Enhanced documentation and code comments, clarifying new features and robustness improvements.

### 0.7.1

- Added `loglog` and `cauchit` distributions to the `LinkFunction` class.
- Renamed the optional module containing the wrapper class `StatsModelsOrderedModel` from `linear` to `parametric`.
- Updated the [license](./LICENSE) file.

### 0.7.0

- Added the `StatsModelsOrderedModel` class, which provides a `scikit-learn` wrapper for the `OrderedModel` class from the `statsmodels` package.
- Added support for custom (user-supplied) link functions.

### 0.6.3

- Improved documentation.

### 0.6.2

- Added link to package vignette on arxiv to ```README.md```.
- Simplified the initialization of fold level models in ```_fit_cv```.
- Fixed a bug in ```_fit_cv``` that prevented using CV-based early stopping with heterogeneous base learners.

### 0.6.1

- Debugged ```_fit_cv``` and ```plot_loss``` methods of ```GradientBoostingOrdinal``` to produce correct plots of training/validation loss, and loss improvement after each g and theta update when using cross-validation for early stopping.
- Enhanced docstrings for ```plot_loss```.

### 0.6.0

- Improved the logic for detecting ```random_state``` as a parameter in the base learners (switching from ```hasattr``` to ```get_params```), as the old method was tricked by sklearn's inheritance mechanics into thinking estimators such as SVM included ```random_state``` as a modifiable parameter.
- Added a utility function, ```generate_heterogeneous_learners```, to stochastically generate a list of base learners to supply to ```GradientBoostingOrdinal``` (heterogenous boosting ensemble).
- Edited code examples in ```README.md``` to reflect the enhancements to the package.
- Enhanced ```load_wine_quality``` to add option for returning X and y - instead of a single dataframe - for red and white datasets.

### 0.5.6

- Tweaked the default hyperparameters of ```DecisionTreeRegressor``` (itself the default ```base_learner``` for ```GradientBoostingOrdinal```) to match those in scikit-learn's ```GradientBoostingClassifier```.
- Small improvements to the ```plot_loss``` method of ```GradientBoostingOrdinal```.
- Added the *Release Notes* section to the ```README.md``` file.
- Small edits to the text and code in ```README.md```.

### 0.5.5

- First public release. 
