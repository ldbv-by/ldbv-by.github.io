# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LDBV-BY'
copyright = '2023, LDBV-BY Doku Team'
author = 'LDBV-BY Doku Team'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.githubpages',
    "nbsphinx"
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'de'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'
html_static_path = ['_static']

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html"]
}

html_theme_options = {
    'nav_title': 'LDBV-BY Dokumentation',
    'logo_icon': '&#xe88e',
    'globaltoc_depth': -1,
}