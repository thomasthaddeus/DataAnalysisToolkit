"""test_data_prep.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import pytest
import numpy as np
import pandas as pd
from src.preprocessor.data_prep import DataPreprocessor

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [10, 20, 30, 40, 50],
        'category': ['A', 'B', 'A', 'B', 'C']
    })

def test_standardize(sample_data):
    preprocessor = DataPreprocessor(sample_data)
    preprocessor.standardize(['feature1', 'feature2'])

    # Test if the mean of the standardized columns is approximately 0
    assert np.isclose(preprocessor.data['feature1'].mean(), 0, atol=0.001)
    assert np.isclose(preprocessor.data['feature2'].mean(), 0, atol=0.001)

    # Test if the standard deviation of the standardized columns is 1
    assert np.isclose(preprocessor.data['feature1'].std(), 1, atol=0.001)
    assert np.isclose(preprocessor.data['feature2'].std(), 1, atol=0.001)

def test_encode_categorical(sample_data):
    preprocessor = DataPreprocessor(sample_data)
    preprocessor.encode_categorical(['category'])

    # Test if the category column is transformed to numerical format
    assert pd.api.types.is_numeric_dtype(preprocessor.data['category'])

# Additional tests for other methods can be added here
