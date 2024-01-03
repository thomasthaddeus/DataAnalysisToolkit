"""test_data_analyzer.py
Summary:
    This script contains tests for the DataAnalysisToolkit class, which is used
    for various data analysis tasks such as calculating statistics, detecting
    outliers, handling missing values, dropping duplicates, encoding categorical
    features, and splitting data into training and testing sets.

Extended Summary:
    Each function in this script is a test that asserts the correctness of a
    corresponding method in the DataAnalysisToolkit class. The tests are written
    using the pytest framework, and can be run using the `pytest` command in the
    terminal.

Returns:
    None: The script does not return anything but prints the test results to the
    terminal. If all tests pass, it means that the DataAnalysisToolkit class is
    functioning as expected.

Raises:
    AssertionError: If a test fails, an AssertionError is raised with a message
    indicating which test failed and why.
"""

import pytest
import pandas as pd
from src.data_analysis_toolkit import DataAnalysisToolkit


@pytest.fixture
def analyzer():
    return DataAnalysisToolkit("../data/test.csv")


def test_calculate_budget_statistics(analyzer):
    """
    Test that calculate_budget_statistics returns a dictionary containing mean,
    median, mode, and trimmed mean.
    """
    statistics = analyzer.calculate_budget_statistics("column_name")
    assert isinstance(statistics, dict)
    assert "mean" in statistics
    assert "median" in statistics
    assert "mode" in statistics
    assert "trimmed_mean" in statistics


def test_detect_outliers(analyzer):
    """
    Test that detect_outliers returns a pandas Series.
    """
    outliers = analyzer.detect_outliers("column_name")
    assert isinstance(outliers, pd.Series)


def test_handle_missing_values(analyzer):
    """
    Test that handle_missing_values correctly fills missing values in the specified column.
    """
    analyzer.handle_missing_values("column_name", strategy="fill", fill_value=0)
    assert analyzer.missing_values["column_name"] == 0


def test_drop_duplicates(analyzer):
    """
    Test that drop_duplicates correctly removes duplicate rows from the
    DataFrame.
    """
    duplicates_before = analyzer.data.duplicated().sum()
    analyzer.drop_duplicates()
    duplicates_after = analyzer.data.duplicated().sum()
    assert duplicates_after < duplicates_before


def test_encode_categorical_features(analyzer):
    """
    Test that encode_categorical_features correctly encodes categorical
    features in the DataFrame.
    """
    analyzer.encode_categorical_features()
    assert (
        analyzer.data[analyzer.categorical_columns]
        .apply(lambda x: x.cat.codes)
        .notnull()
        .all()
        .all()
    )


def test_split_data(analyzer):
    """
    Test that split_data correctly splits the data into training and testing
    sets.
    """
    X_train, X_test, y_train, y_test = analyzer.split_data("target_column")
    assert len(X_train) + len(X_test) == len(analyzer.data)
    assert len(y_train) + len(y_test) == len(analyzer.data)
