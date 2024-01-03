"""data_integrator.py
_summary_

_extended_summary_

Returns:
    _type_: _description_

# Example usage
integrator = DataIntegrator()
integrator.add_data(df1)
integrator.add_data(df2)
combined_data = integrator.join_on_multiple_columns(['column1', 'column2'])
# or
time_series_data = integrator.integrate_time_series('date', method='nearest')
# or
source_data = {'sql': sql_df, 'excel': excel_df, 'api': api_df}
integrated_data = integrator.integrate_from_different_sources(source_data, 'concat')
"""

import pandas as pd


class DataIntegrator:
    """
     _summary_

    _extended_summary_
    """

    def __init__(self):
        """
        Initialize the DataIntegrator.
        """
        self.data_frames = []

    def add_data(self, data_frame):
        """
        Add a DataFrame to the list of data to be integrated.

        Args:
            data_frame (DataFrame): A pandas DataFrame to be added.
        """
        self.data_frames.append(data_frame)

    def concatenate_data(self):
        """
        Concatenate all added DataFrames into a single DataFrame.

        Returns:
            DataFrame: The concatenated DataFrame.
        """
        return pd.concat(self.data_frames, ignore_index=True)

    def merge_data(self, on, how="inner"):
        """
        Merge all added DataFrames into a single DataFrame based on a key
        column.

        Args:
            on (str): Column name to merge on.
            how (str, optional): Type of merge to be performed. Defaults to
            'inner'.

        Returns:
            DataFrame: The merged DataFrame.
        """
        merged_df = self.data_frames[0]
        for df in self.data_frames[1:]:
            merged_df = pd.merge(merged_df, df, on=on, how=how)
        return merged_df

    def join_on_multiple_columns(self, columns, how="inner"):
        """
        Join all added DataFrames on multiple columns.

        Args:
            columns (list of str): List of column names to join on.
            how (str, optional): Type of join to be performed. Defaults to
            'inner'.

        Returns:
            DataFrame: The joined DataFrame.
        """
        joined_df = self.data_frames[0]
        for df in self.data_frames[1:]:
            joined_df = pd.merge(joined_df, df, on=columns, how=how)
        return joined_df

    def integrate_time_series(self, time_column, method="nearest"):
        """
        Integrate time series data from added DataFrames based on a time column.

        Args:
            time_column (str): The name of the time column for integration.
            method (str, optional): Method of time series integration (e.g.,
            'nearest', 'pad'). Defaults to 'nearest'.

        Returns:
            DataFrame: The integrated DataFrame with time series data.
        """
        integrated_df = self.data_frames[0]
        for df in self.data_frames[1:]:
            integrated_df = pd.merge_asof(
                integrated_df, df, on=time_column, method=method
            )
        return integrated_df

    def integrate_from_different_sources(
        self, source_data, integration_method="concat"
    ):
        """
        Integrate data from different sources (like SQL, Excel, APIs).

        Args:
            source_data (dict): A dictionary where keys are source names and
            values are DataFrames.
            integration_method (str, optional): The method of integration
            ('concat', 'merge'). Defaults to 'concat'.

        Returns:
            DataFrame: The integrated DataFrame from different sources.
        """
        self.data_frames = list(source_data.values())
        if integration_method == "concat":
            return self.concatenate_data()
        if integration_method == "merge":
            # Assuming all data frames have a common column for merging
            common_column = source_data.get("common_column")
            return self.merge_data(on=common_column)
