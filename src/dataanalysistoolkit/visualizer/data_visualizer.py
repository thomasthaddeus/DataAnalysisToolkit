"""data_visualizer.py

This module provides a class, DataVisualizer, for creating various data
visualizations. It utilizes matplotlib and seaborn to generate plots such as
box plots, scatter plots, histograms, line plots, pair plots, bar plots, pie
charts, and violin plots

DataVisualizer is designed to work with pandas DataFrames to produce insightful
visualizations. The class offers a range of methods for different types of
plots, making it easier to explore and understand data patterns and
relationships.

Returns:
    _type_: _description_
"""

import json
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    """
    A class for visualizing data using configurations loaded from a JSON file
    and customizable themes.

    This class provides methods for creating different types of plots, such as
    box plots, scatter plots, heatmaps, histograms, line plots, and pair plots.
    It helps in exploring data and extracting insights visually using a
    customizable configuration.

    Attributes:
        data (DataFrame): The pandas DataFrame from which visualizations will
          be generated.
    """
    def __init__(self, data, config_path):
        """
        Initializes the DataVisualizer with the dataset and configuration.

        Args:
            data (DataFrame): The pandas DataFrame to be used for generating
              visualizations.
            config_path (str): Path to the JSON configuration file for plot
              settings.
        """
        self.data = data
        self.set_theme()
        self._load_config(config_path)

    def _load_config(self, config_path):
        """
        Loads the plot configuration from a JSON file.

        Args:
            config_path (str): Path to the configuration file.
        """
        with open(config_path, 'r', encoding='utf-8') as file:
            self.config = json.load(file)
        self.apply_global_style()

    def apply_global_style(self):
        """
        Applies the global style settings from the configuration.
        """
        global_style = self.config.get('global_style', {})
        if 'style' in global_style:
            sns.set_style(global_style['style'])
        if 'context' in global_style:
            sns.set_context(global_style['context'])
        for key, value in global_style.items():
            if key.startswith('figure.') or key.startswith('axes.'):
                plt.rcParams[key] = value

    def apply_plot_style(self, plot_type):
        """
        Applies specific plot style settings, merging them with the global
        style.

        Args:
            plot_type (str): The type of plot for which to apply specific
              styles.
        """
        plot_style = self.config.get(plot_type, {})
        for key, value in plot_style.items():
            plt.rcParams[key] = value

    def set_theme(
        self,
        style="whitegrid",
        context="talk",
        figsize=(12,8),
        titlesize=20,
        labelsize=18,
    ):
        """
        Configures the visual theme for all plots using matplotlib and seaborn.

        Args:
            style (str): The base style of the plots.
            context (str): The context theme of seaborn.
            figsize (list): Size of the figures in inches.
            titlesize (int): Size of the titles.
            labelsize (int): Size of the labels.
        """
        sns.set_style(style)
        sns.set_context(context)
        plt.rcParams["figure.figsize"] = figsize
        plt.rcParams["axes.titlesize"] = titlesize
        plt.rcParams["axes.labelsize"] = labelsize

    def boxplot(self, col, by=None):
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
        self.apply_plot_style("boxplot")
        sns.boxplot(
            x=by,
            y=col,
            data=self.data,
            palette=self.config["boxplot"].get("palette", "deep"),
        )
        plt.show()

    def scatterplot(self, x_col, y_col):
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
        self.apply_plot_style("scatterplot")
        sns.scatterplot(x=x_col, y=y_col, data=self.data)
        plt.show()

    def heatmap(self):
        """
        Generates a heatmap of the correlation matrix of the dataset.

        Heatmaps are useful for visualizing the correlation between different
        variables.

        Returns:
            None: This method shows the plot and does not return a value.
        """
        self.apply_plot_style("heatmap")
        correlation = self.data.corr()
        sns.heatmap(correlation, annot=True)
        plt.show()

    def histogram(self, col):
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
        self.apply_plot_style("histogram")
        sns.histplot(self.data[col])
        plt.show()

    def lineplot(self, x_col, y_col):
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
        self.apply_plot_style("lineplot")
        sns.lineplot(x=x_col, y=y_col, data=self.data)
        plt.show()

    def pairplot(self):
        """
        Generates pair plots for the dataset.

        Pair plots are useful for visualizing pairwise relationships in the
        dataset.

        Returns:
            None: This method shows the plot and does not return a value.
        """
        self.apply_plot_style("pairplot")
        sns.pairplot(self.data)
        plt.show()

    def barplot(self, x_col, y_col):
        """
        Generates a bar plot for two columns.

        Bar plots are useful for comparing different groups or categories.

        Args:
            x_column (str): The name of the column for the x-axis (categorical
            data).
            y_column (str): The name of the column for the y-axis (numerical
            data).

        Returns:
            None: This method shows the plot and does not return a value.
        """
        self.apply_plot_style("barplot")
        sns.barplot(x=x_col, y=y_col, data=self.data)
        plt.show()

    def piechart(self, col):
        """
        Generates a pie chart for a specified column.

        Pie charts are useful for showing the proportion of categories in a
        single categorical variable.

        Args:
            column (str): The name of the categorical column to visualize.

        Returns:
            None: This method shows the plot and does not return a value.
        """
        self.apply_plot_style("piechart")
        pie_data = self.data[col].value_counts()
        plt.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%")
        plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()

    def violinplot(self, col, by=None):
        """
        Generates a violin plot for a specified column.

        Violin plots are useful for visualizing the distribution of data across
        different categories.

        Args:
            column (str): The name of the column for which to generate the
              violin plot.
            by (str, optional): A column name to group data by. Defaults to
              None.

        Returns:
            None: This method shows the plot and does not return a value.
        """
        self.apply_plot_style("violinplot")
        sns.violinplot(x=by, y=col, data=self.data)
        plt.show()
