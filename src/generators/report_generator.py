"""report_generator.py

This module provides a class, ReportGenerator, for generating detailed and
comprehensive reports from datasets. The reports include statistical summaries,
various types of visualizations, and custom text sections, formatted as HTML
for easy interpretation and sharing.

The ReportGenerator class is enhanced to create rich, insightful reports from
pandas DataFrames, suitable for presenting to stakeholders. It includes
functionalities for automatically generating descriptive statistics,
histograms, scatter plots, box plots, and allows for custom written analyses or
notes to be included.
"""

import base64
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class ReportGenerator:
    def __init__(self, data, columns=None):
        """
        Initializes the ReportGenerator with the dataset and optional specific
        columns.

        Args:
            data (DataFrame): The pandas DataFrame from which the report will
            be generated.
            columns (list, optional): Specific columns to be included in the
            report. If None, all columns are used.
        """
        self.data = data
        self.columns = columns if columns else data.columns


    def _generate_base64_image(self, plot_func):
        """
        Helper method to generate a base64 encoded string of a matplotlib plot.

        Args:
            plot_func (function): A function to generate a matplotlib plot.

        Returns:
            str: Base64 encoded string of the plot image.
        """
        buffer = BytesIO()
        plot_func()
        plt.savefig(buffer, format="png")
        plt.close()
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        return base64.b64encode(image_png).decode("utf-8")

    def generate_html_report(self, filename, custom_text=""):
        """
        Generates a comprehensive HTML report of the dataset.

        This method creates an HTML file with statistical summaries, various
        visualizations, and custom text sections for analyses of the dataset.

        Args:
            filename (str): The name of the HTML file to be created.
            custom_text (str, optional): Custom text or analysis to be included in the report.

        Returns:
            None: This method writes to an HTML file and does not return a value.
        """
        report_sections = []

        # Add custom text section
        if custom_text:
            report_sections.append("<h2>Custom Analysis</h2>")
            report_sections.append(f"<p>{custom_text}</p>")

        # Add data description
        report_sections.append("<h2>Data Description</h2>")
        report_sections.append(
            self.data.describe().to_html(classes="table table-striped")
        )

        # Add histograms for all numerical columns
        report_sections.append("<h2>Histograms</h2>")
        for column in self.data.select_dtypes(include=["float64", "int64"]).columns:
            image = self._generate_base64_image(
                lambda: sns.histplot(self.data[column].dropna())
            )
            report_sections.append(
                f'<img src="data:image/png;base64,{image}" alt="Histogram of {column}"><br>'
            )

        # Add scatter plots for pairwise relationships
        report_sections.append('<h2>Scatter Plots</h2>')
        numeric_columns = self.data[self.columns].select_dtypes(include=['float64', 'int64']).columns
        if len(numeric_columns) > 1:
            for i, col1 in enumerate(numeric_columns[:-1]):
                for col2 in numeric_columns[i + 1:]:
                    image = self._generate_base64_image(
                        lambda col1=col1, col2=col2: sns.scatterplot(x=col1, y=col2, data=self.data)
                    )
                    report_sections.append(
                        f'<img src="data:image/png;base64,{image}" alt="Scatter plot of {col1} vs {col2}"><br>'
                    )

        # Add box plots for distributions
        report_sections.append("<h2>Box Plots</h2>")
        for column in numeric_columns:
            image = self._generate_base64_image(
                lambda: sns.boxplot(y=column, data=self.data)
            )
            report_sections.append(
                f'<img src="data:image/png;base64,{image}" alt="Box plot of {column}"><br>'
            )

        # Combine all sections and write to file
        html_content = f"<html><head><title>Data Report</title></head><body>{''.join(report_sections)}</body></html>"
        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(html_content)


# Example usage
# data = pd.read_csv('your_data.csv')
# report_gen = ReportGenerator(data)
# report_gen.generate_html_report('data_report.html', custom_text='Your custom analysis here.')
