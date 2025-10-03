import numpy as np
from ogboost.main import LinkFunctions

def test_probit():
    x = np.array([-1, 0, 1])
    p = LinkFunctions.probit(x)
    x_recovered = LinkFunctions.probit_inverse(p)
    np.testing.assert_allclose(x, x_recovered, atol=1e-5)

def test_logit():
    x = np.array([-1, 0, 1])
    p = LinkFunctions.logit(x)
    x_recovered = LinkFunctions.logit_inverse(p)
    np.testing.assert_allclose(x, x_recovered, atol=1e-5)

def test_cloglog():
    x = np.array([-1, 0, 1])
    p = LinkFunctions.cloglog(x)
    x_recovered = LinkFunctions.cloglog_inverse(p)
    np.testing.assert_allclose(x, x_recovered, atol=1e-5)

from ogboost.main import GradientBoostingOrdinal

def test_model_initialization():
    model = GradientBoostingOrdinal(n_estimators=10, link_function='logit')
    assert model.n_estimators == 10
    assert model.link_function == 'logit'

from sklearn.datasets import make_classification
from ogboost.data import load_wine_quality

def test_fit():
    df_red, _ = load_wine_quality()
    X, y = df_red.drop('quality', axis=1), df_red['quality']
    model = GradientBoostingOrdinal(n_estimators=10)
    model.fit(X, y)
    assert model.classes_.size == y.unique().size
    assert hasattr(model, "_path")

def test_predict_methods():
    df_red, _ = load_wine_quality()
    X, y = df_red.drop('quality', axis=1), df_red['quality']
    model = GradientBoostingOrdinal(n_estimators=10)
    model.fit(X, y)

    preds = model.predict(X)
    assert preds.shape[0] == X.shape[0]

    probs = model.predict_proba(X)
    assert probs.shape == (X.shape[0], model.classes_.size)
    assert np.allclose(probs.sum(axis=1), 1)

def test_end_to_end():
    red, _ = load_wine_quality()
    X = red.drop(columns='quality')
    y = red['quality']

    model = GradientBoostingOrdinal(n_estimators=10)
    model.fit(X, y)

    preds = model.predict(X)
    assert preds.shape[0] == X.shape[0]