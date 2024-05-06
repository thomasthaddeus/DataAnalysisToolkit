#!/bin/bash

# Navigate to the documentation directory
cd docs

# Build the Sphinx Documentation
make html

# Optionally open the documentation in a web browser (on macOS)
open _build/html/index.html
