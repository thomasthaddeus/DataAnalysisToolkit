"""test_data_visualizer.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import pytest
import pandas as pd
import matplotlib.pyplot as plt
from src.visualizer.data_visualizer import DataVisualizer

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'num_col1': [1, 2, 3, 4, 5],
        'num_col2': [5, 4, 3, 2, 1],
        'cat_col': ['A', 'B', 'A', 'B', 'C']
    })

@pytest.fixture
def visualizer(sample_data):
    return DataVisualizer(sample_data)

def test_histogram(visualizer):
    plt.figure()  # Create a new figure
    visualizer.histogram('num_col1')
    # Add assertions or checks if necessary

def test_scatterplot(visualizer):
    plt.figure()
    visualizer.scatterplot('num_col1', 'num_col2')
    # Add assertions or checks if necessary

def test_boxplot(visualizer):
    plt.figure()
    visualizer.boxplot('num_col1')
    # Add assertions or checks if necessary

# Additional tests for other methods
