# Documentation for `generators` Module of DataAnalysisToolkit

The `generators` module in the DataAnalysisToolkit offers a collection of tools for generating synthetic data and comprehensive reports. These tools are especially useful for testing, data processing, and creating visual reports from datasets.

## CSV Data Generator (`csv_data_generator.py`)

### Overview

The `CSVDataGenerator` class is designed to create CSV files with randomly generated data. This functionality is particularly useful for generating test datasets for data processing and machine learning model validation.

### Usage

```python
generator = CSVDataGenerator("data/gen_test.csv", num_rows=500)
generator.generate_csv()
```

### Features

- Generates data with a mix of random integers, floats, dates, times, monetary values, and text.
- Customizable number of rows.
- Randomly includes null values to simulate real-world data scenarios.
- Outputs generated data to a specified CSV file.

### Example

Creating a CSV file with 100 rows of random data:

```python
csv_generator = CSVDataGenerator("output.csv", num_rows=100)
csv_generator.generate_csv()
```

---

## Generate Data (`generate_data.py`)

### Overview Generate Data

The `generate_data` module provides functionality to create a pandas DataFrame with a variety of randomized data types, useful for testing and prototyping.

### Features Generate Data

- Generates random integers, floats, categorical data, and more.
- Includes options for introducing missing values in the data.
- Outputs the generated data as a pandas DataFrame.

### Example Generate Data

Generating a DataFrame with random data and saving it to a CSV file:

```python
df = generate_data(n=200)
df.to_csv("generated_data.csv", index=False)
```

---

## Report Generator (`report_generator.py`)

### Overview Report Generator

The `ReportGenerator` class allows for the generation of detailed HTML reports from pandas DataFrames. These reports include statistical summaries, visualizations, and custom text sections.

### Usage Report Generator

```python
data = pd.read_csv('your_data.csv')
report_gen = ReportGenerator(data)
report_gen.generate_html_report('data_report.html', custom_text='Your custom analysis here.')
```

### Features Report Generator

- Creates reports with statistical summaries like mean, median, mode, and standard deviation.
- Generates histograms, scatter plots, and box plots for data visualization.
- Allows inclusion of custom text or analysis.

### Example Report Generator

Generating an HTML report from a DataFrame:

```python
report_generator = ReportGenerator(df)
report_generator.generate_html_report("report.html", custom_text="Analysis Summary")
```

---

These tools in the `generators` module provide powerful capabilities for creating synthetic data and insightful reports, aiding in data analysis, testing, and presentation tasks.
