"""test_data_analyzer.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import pytest
from data_analyzer import DataAnalyzer


@pytest.fixture
def analyzer():
    return DataAnalyzer("path_to_your_test_file.csv")


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
