# __init__.py

# MIT License
#
# Copyright (c) 2023 Thaddeus Thomas
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Metadata about the package
__version__ = '1.1.1'
__author__ = 'Thaddeus Thomas'
__email__ = 'thaddeus@vcwtech.com'

import logging
import sys

# Convenience imports for users
from .data_analysis_toolkit import DataAnalysisToolkit
from .utils import DataImputer
from .model import FeatureEngineer, ModelEvaluator
from .preprocessor import DataPreprocessor
from .generators import ReportGenerator
from .visualizer import DataVisualizer

# Dependency checks
required_packages = {
    'pandas': '1.1.5',
    'matplotlib': '3.3.4',
    'scipy': '1.6.0',
    'sklearn': '0.24.1'
}

missing_packages = []

for lib, version in required_packages.items():
    try:
        pkg = __import__(lib)
        if pkg.__version__ < version:
            missing_packages.append(f"{lib}>= {version}")
    except ImportError:
        missing_packages.append(f"{lib}>= {version}")

if missing_packages:
    sys.exit("Missing required packages: " + ', '.join(missing_packages))

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Initializing DataAnalysisToolkit package")

# Initialization code that runs on package import, if any
def _init_package():
    # Put any package-wide initialization logic here
    logger.debug("Package initialized successfully")

_init_package()

# Ensure that this module only exposes the intended public interface
__all__ = [
    "DataAnalysisToolkit",
    "DataImputer",
    "DataVisualizer",
    "FeatureEngineer",
    "ModelEvaluator",
    "DataPreprocessor",
    "ReportGenerator"
]
