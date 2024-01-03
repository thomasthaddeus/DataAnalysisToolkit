"""test_generate_data.py
_summary_

_extended_summary_
"""

import pandas as pd
import numpy as np
import pytest
from src.generators.generate_data import df  # Assuming the DataFrame is named 'df' in generate_data.py

def test_column_types():
    assert df['A'].dtype == np.int64
    assert df['B'].dtype == object
    assert df['C'].dtype == float
    assert df['D'].dtype == np.int64
    assert df['E'].dtype == np.int64
    assert df['F'].dtype == object
    assert df['G'].dtype == float
    assert df['H'].dtype == object

def test_column_ranges():
    assert df['A'].between(1, 100).all()
    assert all(letter in "abcdefghij" for letter in df['B'])
    assert df['D'].isin([1, 2, 3]).all()
    assert df['E'].between(1, 100).all()
    assert df['F'].isin(["apple", "banana", "cherry", "date", "elderberry", "fig"]).all()
    assert df['G'].between(1, 5).all()
    assert df['H'].isin(["x", "y", "z"]).all()

def test_missing_values():
    assert df['C'].isna().sum() > 0
    assert df['G'].isna().sum() > 0

# Additional tests for other properties can be added here
