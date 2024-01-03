"""test_feature_engineer.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import pytest
import pandas as pd
from src.model.feature_engineer import FeatureEngineer

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'age': [22, 35, 58, 45, 26],
        'income': [30000, 50000, 80000, 65000, 40000],
        'gender': ['M', 'F', 'F', 'M', 'M']
    })

def test_binning(sample_data):
    engineer = FeatureEngineer(sample_data)
    bins = [20, 30, 40, 50, 60]
    labels = ['20-30', '30-40', '40-50', '50-60']
    engineer.binning('age', bins, labels)

    # Test if binning creates the correct categories
    assert all(engineer.data['binned_age'].isin(labels))

def test_create_interaction(sample_data):
    engineer = FeatureEngineer(sample_data)
    engineer.create_interaction('age', 'income')

    # Test if interaction column is created correctly
    expected_interaction = sample_data['age'] * sample_data['income']
    assert all(engineer.data['interaction_age_income'] == expected_interaction)

# Additional tests for other methods can be added here
