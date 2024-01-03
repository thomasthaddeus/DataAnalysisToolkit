# MIT License
#
# Copyright (c) 2023 Thaddeus Thomas
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""data_analysis_toolkit.py

This module contains a class, DataAnalysisToolkit, for performing various data
analysis tasks on a CSV file. The class is able to load data, calculate various
statistics, detect outliers, handle missing values, drop duplicates, encode
categorical features, split data into training and testing sets, visualize data,
generate reports, preprocess data, and impute missing values.

Example usage:

    from data_analysis_toolkit import DataAnalysisToolkit

    # Initialize the analyzer with the path to a CSV file.
    analyzer = DataAnalysisToolkit('path_to_your_file.csv')

    # Calculate the mean, median, mode, and trimmed mean of a column.
    statistics = analyzer.calculate_budget_statistics('column_name')
    print(statistics)

    # Detect outliers in a column using the z-score method.
    outliers = analyzer.detect_outliers('column_name')
    print(outliers)

    # Handle missing values in a column.
    analyzer.handle_missing_values('column_name', strategy='fill', fill_value=0)

    # Drop duplicate rows in the DataFrame.
    analyzer.drop_duplicates()

    # Encode categorical features in the DataFrame.
    analyzer.encode_categorical_features()

    # Split the data into training and testing sets.
    X_train, X_test, y_train, y_test = analyzer.split_data('target_column')

    # Plot a histogram of a column.
    analyzer.plot_data('column_name')

    # Export the data to a CSV file.
    analyzer.export_data('new_file.csv')

Returns:
    None: This class is used for its side effects of loading, cleaning,
    transforming, and analyzing data, and potentially plotting results.

Raises:
    ValueError: If the CSV file cannot be found, a column name is not found in
    the DataFrame, an unknown outlier detection method or plot type is
    specified, or an inappropriate strategy is chosen for handling missing
    values.
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import trim_mean, zscore
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Importing modules from the project's subdirectories
from generators.report_generator import ReportGenerator
from model.feature_engineer import FeatureEngineer
from model.model_evaluator import ModelEvaluator
from preprocessor.data_prep import DataPreprocessor
from utils.data_imputer import DataImputer
from visualizer.data_visualizer import DataVisualizer


class DataAnalysisToolkit:
    """
    A class to perform various data analysis tasks including loading data,
    calculating statistics, detecting outliers, visualizing data, cleaning data,
    engineering features, splitting data, and exporting data.
    """

    def __init__(self, filename):
        self.data = self.load_data(filename)
        self.visualizer = DataVisualizer(self.data)
        self.imputer = DataImputer(self.data)
        self.preprocessor = DataPreprocessor(self.data)
        self.feature_engineer = FeatureEngineer(self.data)
        self.evaluator = ModelEvaluator(self.data)
        self.report_generator = ReportGenerator(self.data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @property
    def shape(self):
        return self._data.shape

    @property
    def column_names(self):
        return self._data.columns.tolist()

    @property
    def dtypes(self):
        return self._data.dtypes

    @property
    def missing_values(self):
        return self._data.isnull().sum()

    @property
    def numerical_columns(self):
        return self._data.select_dtypes(include=["int64", "float64"]).columns.tolist()

    @property
    def categorical_columns(self):
        return self._data.select_dtypes(include=["object"]).columns.tolist()

    @staticmethod
    def load_data(filename):
        """
        Load data from a CSV file into a DataFrame.

        Args:
            filename (str): The path to the CSV file.

        Returns:
            DataFrame: The loaded data.
        """
        try:
            df = pd.read_csv(filename)
        except FileNotFoundError as exc:
            raise ValueError(f"No such file or directory: '{filename}'") from exc
        return df

    def get_summary_statistics(self):
        """
        Get summary statistics for the DataFrame.

        Returns:
            DataFrame: A DataFrame with the summary statistics.
        """
        return self.data.describe()

    def detect_outliers(self, column_name, method="zscore", threshold=3):
        """
        Detect outliers in a DataFrame using the specified method.

        Args:
            column_name (str): The column to check for outliers.
            method (str, optional): The method to use for outlier detection.
            Default is 'zscore'.
            threshold (float, optional): The threshold to use for outlier
            detection. Default is 3.

        Returns:
            Series: A boolean Series where True indicates an outlier.
        """
        if method == "zscore":
            z_scores = zscore(self.data[column_name])
            return abs(z_scores) > threshold
        else:
            raise ValueError(f"Unknown method: '{method}'")

    def plot_data(self, column_name, plot_type="histogram"):
        """
        Plot data from a DataFrame.

        Args:
            column_name (str): The column to plot.
            plot_type (str, optional): The type of plot to create. Default is
            'histogram'.

        Returns:
            None
        """
        if plot_type == "histogram":
            self.data[column_name].plot(kind="hist")
            plt.title(f"Histogram of {column_name}")
            plt.xlabel(column_name)
            plt.ylabel("Frequency")
            plt.show()
        else:
            raise ValueError(f"Unknown plot type: '{plot_type}'")

    def calculate_budget_statistics(self, column_name, proportiontocut=0.2):
        """
        Calculate and return the mean, median, mode, and trimmed mean of a
        specified column from a CSV file.

        Args:
            column_name (str): The name of the column to analyze.
            proportiontocut (float, optional): The proportion of values to
            remove from each end of the data before calculating the trimmed
            mean. Default is 0.2.

        Returns:
            dict: A dictionary mapping the names of the measures to their
            calculated values.
        """
        if column_name not in self.data.columns:
            raise ValueError(f"'{column_name}' not found in the dataframe.")

        mean_value = self.data[column_name].mean()
        median_value = self.data[column_name].median()
        mode_value = self.data[column_name].mode()[0]
        trmean_value = trim_mean(
            self.data[column_name], proportiontocut=proportiontocut
        )

        return {
            "mean": mean_value,
            "median": median_value,
            "mode": mode_value,
            "trimmed_mean": trmean_value,
        }

    def handle_missing_values(self, column_name, strategy="drop", fill_value=None):
        """
        Handle missing values in a specified column of the DataFrame.

        Args:
            column_name (str): The name of the column to handle missing values.
            strategy (str, optional): The strategy to handle missing values.
                'drop' to drop the rows with missing values,
                'fill' to fill missing values with 'fill_value'.
                Default is 'drop'.
            fill_value (scalar, optional): The value to use when filling
                missing values. Required if strategy is 'fill'.

        Returns:
            None
        """
        if strategy == "drop":
            self._data.dropna(subset=[column_name], inplace=True)
        elif strategy == "fill":
            if fill_value is None:
                raise ValueError("fill_value must be provided when strategy is 'fill'.")
            self._data[column_name].fillna(fill_value, inplace=True)
        else:
            raise ValueError(
                "Unknown strategy: '{strategy}'. Available strategies are 'drop' and 'fill'."
            )

    def drop_duplicates(self, subset=None, keep="first"):
        """
        Drop duplicate rows in the DataFrame.

        Args:
            subset (list-like, optional): Only consider certain columns for
            identifying duplicates. By default all of the columns are used.
            keep ({'first', 'last', False}, default 'first'): Determines which
            duplicates (if any) to keep. 'first' : Drop duplicates except for
            the first occurrence. 'last' : Drop duplicates except for the last
            occurrence. False : Drop all duplicates.

        Returns:
            None
        """
        self._data.drop_duplicates(subset=subset, keep=keep, inplace=True)

    def split_data(self, target_column, test_size=0.2, random_state=None):
        """
        Split the data into training and testing sets.

        Args:
            target_column (str): The name of the target (dependent) column.
            test_size (float, optional): The proportion of the dataset to
            include in the test split. Default is 0.2.
            random_state (int, optional): Controls the shuffling applied to the
            data before applying the split. Pass an int for reproducible output
            across multiple function calls.

        Returns:
            tuple: A tuple containing the training and testing data (X_train,
            X_test, y_train, y_test).
        """
        X = self._data.drop(target_column, axis=1)
        y = self._data[target_column]
        return train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

    def encode_categorical_features(self):
        """
        Encode categorical features in the DataFrame.

        Returns:
            None
        """
        le = LabelEncoder()
        for col in self.categorical_columns:
            self._data[col] = le.fit_transform(self._data[col])

    def export_data(self, filename, index=False):
        """
        Export the data to a CSV file.

        Args:
            filename (str): The name of the file to export the data.
            index (bool, optional): Write row names (index). Default is False.

        Returns:
            None
        """
        self._data.to_csv(filename, index=index)
