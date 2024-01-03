"""test_report_generator.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import os
import pytest
import pandas as pd
from src.generators.report_generator import ReportGenerator

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'age': [25, 30, 35, 40, 45],
        'salary': [50000, 60000, 70000, 80000, 90000],
        'department': ['HR', 'Marketing', 'IT', 'Finance', 'Admin']
    })

def test_generate_html_report(sample_data, tmp_path):
    report_generator = ReportGenerator(sample_data)
    report_file = tmp_path / "report.html"

    report_generator.generate_html_report(str(report_file))

    # Test if the file was created
    assert report_file.exists()

    # Optional: Test contents of the report
    with open(report_file, "r") as file:
        contents = file.read()
        assert 'age' in contents
        assert 'salary' in contents
        assert 'department' in contents

# Additional tests for other methods or features can be added here
