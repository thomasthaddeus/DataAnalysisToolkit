# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Data Analysis Toolkit'
copyright = '2024, Thaddeus Thomas'
author = 'Thaddeus Thomas'
release = '1.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'nbsphinx'
]

templates_path = ['docs/_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['docs/_static']

html_sidebars = {
   '**': [
       'about.html',
       'navigation.html',
       'relations.html',
       'searchbox.html',
       'donate.html',
   ]
}

# -- Extension configuration -------------------------------------------------

# Configuration for nbsphinx
nbsphinx_execute = 'never'  # Do not execute notebooks automatically

# Other configurations can be added as needed
