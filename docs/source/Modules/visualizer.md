# Documentation for `visualizer` Module of DataAnalysisToolkit

The `visualizer` module in DataAnalysisToolkit offers a suite of tools for creating various types of data visualizations. It leverages libraries like matplotlib and seaborn to generate insightful plots from pandas DataFrames.

## Data Visualizer (`data_visualizer.py`)

### Overview

The `DataVisualizer` class is designed for generating a wide range of visualizations to explore and understand data patterns and relationships. It includes methods for creating box plots, scatter plots, heatmaps, histograms, line plots, pair plots, bar plots, pie charts, and violin plots.

### Usage

```python
visualizer = DataVisualizer(df)
visualizer.boxplot('salary', by='department')
visualizer.scatterplot('age', 'salary')
visualizer.heatmap()
```

### Methods

- `__init__(self, data)`: Initialize the DataVisualizer with a dataset.
- `boxplot(self, column, by=None)`: Generate a box plot for a specified column.
- `scatterplot(self, x_column, y_column)`: Create a scatter plot between two columns.
- `heatmap(self)`: Produce a heatmap of the correlation matrix of the dataset.
- `histogram(self, column)`: Create a histogram for a specified column.
- `lineplot(self, x_column, y_column)`: Generate a line plot between two columns.
- `pairplot(self)`: Create pair plots for the dataset.
- `barplot(self, x_column, y_column)`: Produce a bar plot for two columns.
- `piechart(self, column)`: Generate a pie chart for a specified column.
- `violinplot(self, column, by=None)`: Create a violin plot for a specified column.

### Examples

Creating a Histogram and a Scatter Plot:

```python
data_visualizer = DataVisualizer(df)
data_visualizer.histogram('age')
data_visualizer.scatterplot('height', 'weight')
```

Generating a Heatmap and a Pair Plot:

```python
visualizer = DataVisualizer(df)
visualizer.heatmap()
visualizer.pairplot()
```

Creating a Bar Plot and a Pie Chart:

```python
visualizer = DataVisualizer(df)
visualizer.barplot('department', 'salary')
visualizer.piechart('department')
```

---

The `visualizer` module is a key component of the DataAnalysisToolkit, offering a variety of visualization options to help users gain deeper insights into their data. These visualization tools are crucial for data exploration, allowing users to uncover patterns, trends, and relationships in their datasets effectively.
