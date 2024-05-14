"""statistical_analysis/statistics.py
_summary_

_extended_summary_

Returns:
    _type_: _description_

# Usage
stats = Statistics_1([1, 2, 3, 4, 5, 5, 2])
stats.add_paired_data(1, 2)
stats.add_paired_data(2, 3)
stats.add_paired_data(3, 6)
stats.add_paired_data(4, 8)
print(
    f"Mean: {stats.mean()}\n",
    f"Median: {stats.median()}\n",
    f"Mode: {stats.mode()}\n",
    f"Variance: {stats.variance()}\n",
    f"Standard Deviation: {stats.standard_deviation()}\n",
    f"Quantile (0.5): {stats.quantile(0.5)}\n",
    f"Linear Regression (Slope, Intercept): {stats.simple_linear_regression()}\n",
)
"""

import statistics
from collections import Counter

class Statistics_1:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data
        self.paired_data = []

    def add_data(self, value):
        """ Adds a new value to the data list. """
        self.data.append(value)

    def add_paired_data(self, x, y):
        """ Adds a new paired data point (x, y). """
        self.paired_data.append((x, y))

    def mean(self):
        """ Returns the mean of the data. """
        if not self.data:
            return None
        return sum(self.data) / len(self.data)

    def median(self):
        """ Returns the median of the data. """
        if not self.data:
            return None
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        """ Returns the mode of the data. If multiple modes, returns a list of modes. """
        if not self.data:
            return None
        data_counter = Counter(self.data)
        max_count = max(data_counter.values())
        return [num for num, count in data_counter.items() if count == max_count]

    def variance(self):
        """ Returns the variance of the data. """
        if not self.data:
            return None
        mu = self.mean()
        return sum((x - mu) ** 2 for x in self.data) / len(self.data)

    def standard_deviation(self):
        """ Returns the standard deviation of the data. """
        return self.variance() ** 0.5

    def quantile(self, q):
        """ Returns the q-th quantile of the data. """
        if not self.data:
            return None
        sorted_data = sorted(self.data)
        index = int(len(sorted_data) * q)
        return sorted_data[index]

    def quantile_linear_interpolation(self, q):
        """ Returns the q-th quantile of the data, with linear interpolation if necessary. """
        if not self.data:
            return None
        sorted_data = sorted(self.data)
        position = (len(sorted_data) - 1) * q
        floor_index = int(position)
        ceil_index = floor_index + 1

        if ceil_index >= len(sorted_data):
            return sorted_data[floor_index]
        else:
            lower_value = sorted_data[floor_index]
            upper_value = sorted_data[ceil_index]
            return lower_value + (upper_value - lower_value) * (position - floor_index)

    def simple_linear_regression(self):
        """ Returns the slope and intercept for simple linear regression of paired data. """
        if not self.paired_data:
            return None, None
        n = len(self.paired_data)
        sum_x = sum(x for x, y in self.paired_data)
        sum_y = sum(y for x, y in self.paired_data)
        sum_xy = sum(x * y for x, y in self.paired_data)
        sum_x2 = sum(x ** 2 for x, y in self.paired_data)

        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        intercept = (sum_y - slope * sum_x) / n
        return slope, intercept


# Usage
stats = Statistics_1([1, 2, 3, 4, 5, 5, 2])
stats.add_paired_data(1, 2)
stats.add_paired_data(2, 3)
stats.add_paired_data(3, 6)
stats.add_paired_data(4, 8)
print(
    f"Mean: {stats.mean()}\n",
    f"Median: {stats.median()}\n",
    f"Mode: {stats.mode()}\n",
    f"Variance: {stats.variance()}\n",
    f"Standard Deviation: {stats.standard_deviation()}\n",
    f"Quantile (0.25): {stats.quantile(0.25)}\n",
    f"Quantile (0.50): {stats.quantile(0.50)}\n",
    f"Quantile (0.75): {stats.quantile(0.75)}\n",
    f"Quantile (0.25): {stats.quantile_linear_interpolation(0.25):.4f}\n",
    f"Quantile (0.50): {stats.quantile_linear_interpolation(0.50):.4f}\n",
    f"Quantile (0.75): {stats.quantile_linear_interpolation(0.75):.4f}\n",
    f"Linear Regression (Slope, Intercept): {stats.simple_linear_regression()}\n",
)
