import numpy as np
import pytest
from sklearn.ensemble import RandomForestClassifier

from ml.data import apply_label
from ml.model import (
    compute_model_metrics,
    inference,
    train_model,
)


@pytest.fixture
def sample_training_data():
    """
    Create a small binary classification dataset for testing.
    """
    X = np.array(
        [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1],
            [2, 0],
            [2, 1],
            [3, 0],
            [3, 1],
        ]
    )
    y = np.array([0, 0, 0, 1, 1, 1, 1, 1])
    return X, y


@pytest.fixture
def trained_model(sample_training_data):
    """
    Train a model that can be reused by multiple tests.
    """
    X, y = sample_training_data
    return train_model(X, y)


def test_train_model_uses_random_forest(trained_model):
    """
    Confirm that train_model returns a fitted random forest classifier.
    """
    assert isinstance(trained_model, RandomForestClassifier)
    assert hasattr(trained_model, "classes_")


def test_inference_returns_expected_shape(
    trained_model,
    sample_training_data,
):
    """
    Confirm that inference returns one prediction per input row.
    """
    X, _ = sample_training_data
    predictions = inference(trained_model, X)

    assert isinstance(predictions, np.ndarray)
    assert predictions.shape == (len(X),)
    assert set(predictions).issubset({0, 1})


def test_compute_model_metrics_returns_expected_values():
    """
    Confirm precision, recall, and F1 calculations.
    """
    labels = np.array([1, 1, 0, 0])
    predictions = np.array([1, 0, 1, 0])

    precision, recall, fbeta = compute_model_metrics(
        labels,
        predictions,
    )

    assert precision == pytest.approx(0.5)
    assert recall == pytest.approx(0.5)
    assert fbeta == pytest.approx(0.5)


def test_apply_label_returns_salary_categories():
    """
    Confirm that binary predictions become readable salary labels.
    """
    assert apply_label(np.array([1])) == ">50K"
    assert apply_label(np.array([0])) == "<=50K"
