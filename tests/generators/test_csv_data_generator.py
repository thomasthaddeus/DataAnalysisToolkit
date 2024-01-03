"""test_csv_data_generator.py
_summary_

_extended_summary_

Returns:
    _type_: _description_
"""

import os
import csv
import datetime
import pytest
from src.generators.csv_data_generator import CSVDataGenerator

def test_csv_file_creation(tmp_path):
    # Create a temporary file path
    temp_file = tmp_path / "test_data.csv"

    # Initialize CSVDataGenerator with the temporary file path
    generator = CSVDataGenerator(str(temp_file), num_rows=100)
    generator.generate_csv()

    # Check if file was created
    assert os.path.exists(temp_file)

def test_csv_file_structure(tmp_path):
    temp_file = tmp_path / "test_data.csv"
    generator = CSVDataGenerator(str(temp_file), num_rows=10)
    generator.generate_csv()

    with open(temp_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        expected_headers = [
            "Integer", "Float", "Text1", "Text2", "Text3", "Text4", "Text5",
            "Date", "Time", "Money"
        ]
        assert headers == expected_headers

        # Check the number of rows and data types
        for row in reader:
            assert len(row) == len(expected_headers)
            assert row[0].isdigit() or row[0] is None  # Integer
            assert is_float(row[1]) or row[1] is None  # Float
            assert is_date(row[7]) or row[7] is None  # Date
            assert is_time(row[8]) or row[8] is None  # Time
            assert is_float(row[9]) or row[9] is None  # Money

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_date(value):
    try:
        datetime.datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_time(value):
    try:
        datetime.datetime.strptime(value, "%H:%M")
        return True
    except ValueError:
        return False
