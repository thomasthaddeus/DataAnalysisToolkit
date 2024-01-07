### Documentation for `integrators` Module of DataAnalysisToolkit

The `integrators` module in DataAnalysisToolkit provides tools for integrating and combining data from various sources into a unified format. This is particularly useful for creating comprehensive datasets by merging data from different sources like SQL databases, Excel files, and APIs.

#### Data Integrator (`data_integrator.py`)

##### Overview

The `DataIntegrator` class allows for seamless integration of multiple pandas DataFrames. It supports various methods of integration, including concatenation, merging on key columns, joining on multiple columns, and time-series integration.

##### Usage

```python
integrator = DataIntegrator()
integrator.add_data(df1)
integrator.add_data(df2)
combined_data = integrator.concatenate_data()
```

##### Methods

- `__init__(self)`: Initialize the Data Integrator.
- `add_data(self, data_frame)`: Add a DataFrame to be integrated.
- `concatenate_data(self)`: Concatenate all added DataFrames into a single DataFrame.
- `merge_data(self, on, how="inner")`: Merge DataFrames based on a key column.
- `join_on_multiple_columns(self, columns, how="inner")`: Join DataFrames on multiple columns.
- `integrate_time_series(self, time_column, method="nearest")`: Integrate time-series data based on a time column.
- `integrate_from_different_sources(self, source_data, integration_method="concat")`: Integrate data from different sources.

##### Examples

Concatenating DataFrames:

```python
integrator = DataIntegrator()
integrator.add_data(df1)
integrator.add_data(df2)
concatenated_df = integrator.concatenate_data()
```

Merging DataFrames on a Common Key:

```python
integrator = DataIntegrator()
integrator.add_data(df1)
integrator.add_data(df2)
merged_df = integrator.merge_data(on='common_key')
```

Time-Series Integration:

```python
integrator = DataIntegrator()
integrator.add_data(time_series_df1)
integrator.add_data(time_series_df2)
time_series_combined = integrator.integrate_time_series('timestamp', method='nearest')
```

Integrating Data from Different Sources:

```python
source_data = {'source1': df1, 'source2': df2}
integrator = DataIntegrator()
combined_source_data = integrator.integrate_from_different_sources(source_data)
```

---

The `DataIntegrator` is a powerful tool for combining data in various ways, making it easier to prepare comprehensive datasets for analysis. This flexibility is crucial when dealing with data from multiple sources or formats.
