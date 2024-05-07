#!/bin/bash

# renders the documentation
sphinx-build -M html docs/source/ docs/build/

# Navigate to the documentation directory
cd docs

# Build the Sphinx Documentation
make html

# Optionally open the documentation in a web browser (on macOS)
open _build/html/index.html
