"""feature_engineer.py

This module provides a class, FeatureEngineer, for engineering new features in
datasets. Feature engineering is a critical step in data preprocessing for
machine learning, as it involves creating new features from the existing data
to improve model performance.

The FeatureEngineer class is designed to facilitate common feature engineering
tasks such as binning numerical data into categories and creating interaction
features (multiplying two features together). These operations can help uncover
insights and patterns in the data that are not apparent in the original
features.
"""

import pandas as pd

class FeatureEngineer:
    """
    A class for performing feature engineering on datasets.

    This class provides methods for common feature engineering tasks, such as
    binning values and creating interaction features. These functionalities are
    important for preparing datasets for more effective machine learning
    modeling.

    Attributes:
        data (DataFrame): The dataset on which feature engineering tasks will be performed.
    """

    def __init__(self, data):
        """
        Initializes the FeatureEngineer object with the dataset.

        Args:
            data (DataFrame): The dataset to be used for feature engineering.
                              It should be a Pandas DataFrame.
        """
        self.data = data

    def binning(self, column, bins, labels):
        """
        Performs binning on a specified column of the dataset.

        Binning is the process of transforming continuous numerical variables
        into discrete categories (bins). This method divides a column into
        different bins and assigns corresponding labels to these bins.

        Args:
            column (str): The name of the column to be binned.
            bins (list of numbers): The edges defining the bins.
            labels (list of str): The labels for each bin.

        Returns:
            None: The method adds the binned column to the dataset in place and
            does not return anything.
        """
        self.data[f'binned_{column}'] = pd.cut(self.data[column], bins=bins, labels=labels)

    def create_interaction(self, column1, column2):
        """
        Creates an interaction feature from two columns.

        This method multiplies two columns together to create a new interaction
        feature. Interaction features can capture the combined effect of two
        variables which might not be apparent when considered separately.

        Args:
            column1 (str): The name of the first column to be used in the
            interaction.
            column2 (str): The name of the second column to be used in the
            interaction.

        Returns:
            None: The method adds the interaction feature to the dataset in
            place and does not return anything.
        """
        self.data[f'interaction_{column1}_{column2}'] = self.data[column1] * self.data[column2]
