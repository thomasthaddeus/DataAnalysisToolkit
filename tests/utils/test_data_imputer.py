"""test_data_imputer.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import pytest
import pandas as pd
import numpy as np
from src.utils.data_imputer import DataImputer

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'num_col': [1, np.nan, 3, np.nan, 5],
        'cat_col': ['A', 'B', np.nan, 'B', 'C'],
        'const_col': [np.nan, np.nan, np.nan, np.nan, np.nan]
    })

def test_mean_imputation(sample_data):
    imputer = DataImputer(sample_data)
    imputer.mean_imputation(['num_col'])
    assert not imputer.data['num_col'].isnull().any()
    assert imputer.data['num_col'][1] == pytest.approx(3.0)  # Approximate mean

def test_median_imputation(sample_data):
    imputer = DataImputer(sample_data)
    imputer.median_imputation(['num_col'])
    assert not imputer.data['num_col'].isnull().any()
    assert imputer.data['num_col'][1] == 3.0  # Median value

def test_most_frequent_imputation(sample_data):
    imputer = DataImputer(sample_data)
    imputer.most_frequent_imputation(['cat_col'])
    assert not imputer.data['cat_col'].isnull().any()
    assert imputer.data['cat_col'][2] == 'B'  # Most frequent value

def test_constant_imputation(sample_data):
    imputer = DataImputer(sample_data)
    imputer.constant_imputation(['const_col'], fill_value=0)
    assert not imputer.data['const_col'].isnull().any()
    assert imputer.data['const_col'].equals(pd.Series([0, 0, 0, 0, 0]))

# Additional tests can be added for other scenarios and methods
