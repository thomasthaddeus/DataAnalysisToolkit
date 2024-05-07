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
__version__ = '1.2.2'
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
    "certifi": "2024.2.2",
    "charset-normalizer": "3.3.2",
    "click": "8.1.7",
    "colorama": "0.4.6",
    "contourpy": "1.2.1",
    "cycler": "0.12.1",
    "docutils": "0.21.2",
    "fonttools": "4.51.0",
    "greenlet": "3.0.3",
    "idna": "3.7",
    "importlib_metadata": "7.1.0",
    "joblib": "1.4.2",
    "keyring": "25.2.0",
    "kiwisolver": "1.4.5",
    "markdown-it-py": "3.0.0",
    "matplotlib": "3.8.4",
    "mdurl": "0.1.2",
    "more-itertools": "10.2.0",
    "nh3": "0.2.17",
    "nltk": "3.8.1",
    "numpy": "1.26.4",
    "packaging": "24.0",
    "pandas": "2.2.2",
    "pillow": "10.3.0",
    "pkginfo": "1.10.0",
    "Pygments": "2.18.0",
    "pyparsing": "3.1.2",
    "pyproject_hooks": "1.1.0",
    "python-dateutil": "2.9.0.post0",
    "pytz": "2024.1",
    "pywin32-ctypes": "0.2.2",
    "readme_renderer": "43.0",
    "regex": "2024.4.28",
    "requests": "2.31.0",
    "requests-toolbelt": "1.0.0",
    "rfc3986": "2.0.0",
    "rich": "13.7.1",
    "scikit-learn": "1.4.2",
    "scipy": "1.13.0",
    "seaborn": "0.13.2",
    "six": "1.16.0",
    "SQLAlchemy": "2.0.30",
    "threadpoolctl": "3.5.0",
    "tqdm": "4.66.4",
    "typing_extensions": "4.11.0",
    "tzdata": "2024.1",
    "urllib3": "2.2.1",
    "zipp": "3.18.1",
}

missing_packages = []

for lib, version in required_packages.items():
    try:
        pkg = __import__(lib)
        # Safely get the version or None if not available
        pkg_version = getattr(pkg, '__version__', None)
        if not pkg_version or pkg_version < version:
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
