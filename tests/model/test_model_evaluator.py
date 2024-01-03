"""test_model_evaluator.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import pytest
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from src.model.model_evaluator import ModelEvaluator
from sklearn.metrics import confusion_matrix, precision_score, recall_score

@pytest.fixture
def sample_data():
    X, y = make_classification(n_samples=100, n_features=4, random_state=42)
    return train_test_split(X, y, test_size=0.2, random_state=42)

@pytest.fixture
def trained_model(sample_data):
    X_train, X_test, y_train, y_test = sample_data
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    return model, X_test, y_test

def test_confusion_matrix(trained_model):
    model, X_test, y_test = trained_model
    evaluator = ModelEvaluator(model, X_test, y_test)
    predicted_cm = evaluator.get_confusion_matrix()
    expected_cm = confusion_matrix(y_test, model.predict(X_test))

    assert (predicted_cm == expected_cm).all()

def test_precision(trained_model):
    model, X_test, y_test = trained_model
    evaluator = ModelEvaluator(model, X_test, y_test)
    predicted_precision = evaluator.get_precision()
    expected_precision = precision_score(y_test, model.predict(X_test))

    assert predicted_precision == pytest.approx(expected_precision)

def test_recall(trained_model):
    model, X_test, y_test = trained_model
    evaluator = ModelEvaluator(model, X_test, y_test)
    predicted_recall = evaluator.get_recall()
    expected_recall = recall_score(y_test, model.predict(X_test))

    assert predicted_recall == pytest.approx(expected_recall)

# Additional tests for other methods can be added here
