"""data_visualizer.py

This module provides a class, DataVisualizer, for creating various data
visualizations. It utilizes matplotlib and seaborn to generate plots such as
box plots, scatter plots, histograms, line plots, pair plots, bar plots, pie
charts, and violin plots

DataVisualizer is designed to work with pandas DataFrames to produce insightful
visualizations. The class offers a range of methods for different types of
plots, making it easier to explore and understand data patterns and
relationships.
"""

import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    """
    A class for visualizing data in various forms.

    This class provides methods for creating different types of plots, such as
    box plots, scatter plots, heatmaps, histograms, line plots, and pair plots.
    It helps in exploring data and extracting insights visually.

    Attributes:
        data (DataFrame): The pandas DataFrame from which visualizations will
        be generated.
    """
    def __init__(self, data):
        """
        Initializes the DataVisualizer with the dataset.

        Args:
            data (DataFrame): The pandas DataFrame to be used for generating
            visualizations.
        """
        self.data = data

    def boxplot(self, column, by=None):
        """
        Generates a box plot for a specified column.

        Box plots are useful for visualizing the distribution of data and
        identifying outliers.

        Args:
            column (str): The name of the column for which to generate the box
            plot.
            by (str, optional): A column name to group data by. Defaults to
            None.

        Returns:
            None: This method shows the plot and does not return a value.
        """
        sns.boxplot(x=by, y=column, data=self.data)
        plt.show()

    def scatterplot(self, x_column, y_column):
        """
        Generates a scatter plot between two columns.

        Scatter plots are useful for visualizing the relationship between two
        variables.

        Args:
            x_column (str): The name of the column for the x-axis.
            y_column (str): The name of the column for the y-axis.

        Returns:
            None: This method shows the plot and does not return a value.
        """
        sns.scatterplot(x=x_column, y=y_column, data=self.data)
        plt.show()

    def heatmap(self):
        """
        Generates a heatmap of the correlation matrix of the dataset.

        Heatmaps are useful for visualizing the correlation between different
        variables.

        Returns:
            None: This method shows the plot and does not return a value.
        """
        correlation = self.data.corr()
        sns.heatmap(correlation, annot=True)
        plt.show()

    def histogram(self, column):
        """
        Generates a histogram for a specified column.

        Histograms are useful for visualizing the distribution of a single
        variable.

        Args:
            column (str): The name of the column for which to generate the
            histogram.

        Returns:
            None: This method shows the plot and does not return a value.
        """
        sns.histplot(self.data[column])
        plt.show()

    def lineplot(self, x_column, y_column):
        """
        Generates a line plot between two columns.

        Line plots are useful for visualizing data trends over time or ordered
        categories.

        Args:
            x_column (str): The name of the column for the x-axis.
            y_column (str): The name of the column for the y-axis.

        Returns:
            None: This method shows the plot and does not return a value.
        """
        sns.lineplot(x=x_column, y=y_column, data=self.data)
        plt.show()

    def pairplot(self):
        """
        Generates pair plots for the dataset.

        Pair plots are useful for visualizing pairwise relationships in the
        dataset.

        Returns:
            None: This method shows the plot and does not return a value.
        """
        sns.pairplot(self.data)
        plt.show()

    def barplot(self, x_column, y_column):
        """
        Generates a bar plot for two columns.

        Bar plots are useful for comparing different groups or categories.

        Args:
            x_column (str): The name of the column for the x-axis (categorical data).
            y_column (str): The name of the column for the y-axis (numerical data).

        Returns:
            None: This method shows the plot and does not return a value.
        """
        sns.barplot(x=x_column, y=y_column, data=self.data)
        plt.show()

    def piechart(self, column):
        """
        Generates a pie chart for a specified column.

        Pie charts are useful for showing the proportion of categories in a single categorical variable.

        Args:
            column (str): The name of the categorical column to visualize.

        Returns:
            None: This method shows the plot and does not return a value.
        """
        pie_data = self.data[column].value_counts()
        plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    def violinplot(self, column, by=None):
        """
        Generates a violin plot for a specified column.

        Violin plots are useful for visualizing the distribution of data across different categories.

        Args:
            column (str): The name of the column for which to generate the violin plot.
            by (str, optional): A column name to group data by. Defaults to None.

        Returns:
            None: This method shows the plot and does not return a value.
        """
        sns.violinplot(x=by, y=column, data=self.data)
        plt.show()
