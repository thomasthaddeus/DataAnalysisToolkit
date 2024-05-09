# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
# from dataanalysistoolkit import __version__, __author__
sys.path.insert(0, os.path.abspath('../../src/dataanalysistoolkit/'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Data Analysis Toolkit'
copyright = '2024, Thaddeus Thomas'  # pylint: disable=W0622
author = 'Thaddeus Thomas'
release = '1.2.3'
version = '1.2.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'nbsphinx'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
html_static_path = ['_static']

html_sidebars = {
   '**': [
       'about.html',
       'donate.html',
       'navigation.html',
       'relations.html',
       'sourcelink.html',
       'searchbox.html',
   ]
}

# -- Extension configuration -------------------------------------------------

# Configuration for nbsphinx
nbsphinx_execute = 'never'  # Do not execute notebooks automatically

# Other configurations can be added as needed
