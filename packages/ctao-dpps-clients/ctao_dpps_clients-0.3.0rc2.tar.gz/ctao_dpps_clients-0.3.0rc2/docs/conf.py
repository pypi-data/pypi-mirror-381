"""
Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

from dpps import __version__

# -- Project information -----------------------------------------------------

project = "DPPS"
copyright = "CTAO"
author = "Data Processing and Preservation System"
version = __version__
release = version
today_fmt = "%Y-%m-%d"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "numpydoc",
    "myst_parser",
    "sphinx_changelog",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["changes/*"]

# have all links automatically associated with the right domain.
default_role = "py:obj"


# intersphinx allows referencing other packages sphinx docs
intersphinx_mapping = {}

# -- Options for HTML output -------------------------------------------------

html_theme = "ctao"
html_theme_options = dict(
    navigation_with_keys=False,
    logo=dict(
        text="DPPS",
    ),
    # setup for displaying multiple versions, also see setup in .gitlab-ci.yml
    switcher=dict(
        json_url="http://cta-computing.gitlab-pages.cta-observatory.org/dpps/dpps/versions.json",  # noqa: E501
        version_match="latest" if ".dev" in version else f"v{version}",
    ),
    navbar_center=["version-switcher", "navbar-nav"],
)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
