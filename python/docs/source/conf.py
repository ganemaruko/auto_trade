# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
# sys.path.insert(0, os.path.abspath("../"))
sys.path.insert(0, os.path.abspath("../../env/"))
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'auto_trade'
copyright = '2023, ganemaruko'
author = 'ganemaruko'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',  # ref: https://zenn.dev/utahka/articles/df9713f4ac990d
    'sphinx.ext.napoleon'  # ref: https://www.sphinx-doc.org/ja/master/usage/extensions/napoleon.html
]

templates_path = ['_templates']
exclude_patterns = []

language = 'jp'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pyramid'
html_static_path = ['_static']
