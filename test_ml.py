import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import train_model, compute_model_metrics, inference

# Load data for testing
import pandas as pd
data = pd.read_csv('data/census.csv')
cat_features = ["workclass", "education", "marital-status", "occupation",
                "relationship", "race", "sex", "native-country"]
X, y, encoder, lb = process_data(data, categorical_features=cat_features, label="salary", training=True)

# Implement the first test
def test_train_model():
    """
    Test if the train_model function returns a RandomForestClassifier.
    """
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier), "Model is not a RandomForestClassifier"

# Implement the second test
def test_inference():
    """
    Test if the inference function returns the expected type of result.
    """
    model = train_model(X, y)
    preds = inference(model, X)
    assert isinstance(preds, np.ndarray), "Inference does not return np.ndarray"

# Implement the third test
def test_compute_model_metrics():
    """
    Test if the compute_model_metrics function returns expected values.
    """
    model = train_model(X, y)
    preds = inference(model, X)
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert isinstance(precision, float), "Precision is not a float"
    assert isinstance(recall, float), "Recall is not a float"
    assert isinstance(fbeta, float), "Fbeta is not a float"
    assert 0 <= precision <= 1, "Precision out of bounds"
    assert 0 <= recall <= 1, "Recall out of bounds"
    assert 0 <= fbeta <= 1, "Fbeta out of bounds"
