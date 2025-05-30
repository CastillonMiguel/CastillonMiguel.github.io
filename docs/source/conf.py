# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
project = 'Miguel Castillón'
copyright = '2024, Miguel Castillón'
author = 'Miguel Castillón'

# The full version, including alpha/beta/rc tags
release = '0.1'
language = "en"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# from sphinx_gallery.sorting import FileNameSortKey

extensions = [
    'sphinx.ext.autodoc',
    'numpydoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.autosummary',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'IPython.sphinxext.ipython_console_highlighting',
    'IPython.sphinxext.ipython_directive',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
    'sphinx_math_dollar',
    'matplotlib.sphinxext.plot_directive',
    "sphinx_design"
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
html_context = {
   "default_mode": "dark"   # light dark auto
}

html_sidebars = {
    "**": ["sidebar-nav-bs", "sidebar-ethical-ads"],
    "index": [],
    "AboutMe/index": [],
    "Projects/index": [],
    "Publications/index": [],
    "Art/index": [],
    "Contact/index": [],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = '_static/Image.png'


# Disable the "Show Source" link
html_show_sphinx = False
html_show_sourcelink = False
html_theme_options = {
    "external_links": [],
    "footer_start": ["sphinx-version"],
    "github_url": "https://github.com/CastillonMiguel",
    "navbar_align": "left",
    "icon_links": [
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/miguelcastillon",
            "icon": "fa-brands fa-linkedin",
        },
    ],
}
