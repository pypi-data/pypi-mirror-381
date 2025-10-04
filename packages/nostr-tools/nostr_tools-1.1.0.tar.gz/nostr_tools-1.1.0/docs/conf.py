# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path

# Add project source to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

# -- Project information -----------------------------------------------------

project = "nostr-tools"
copyright = "Bigbrotr"
author = "Bigbrotr"

# The version info from setuptools-scm
try:
    from nostr_tools import __version__

    version = __version__
    release = __version__
except ImportError:
    version = "development"
    release = "development"

# -- General configuration ---------------------------------------------------

extensions = [
    # Sphinx built-in extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx.ext.coverage",  # Documentation coverage tracking
    # Third-party extensions
    "myst_parser",  # For Markdown support
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Source file suffixes
source_suffix = {
    ".rst": None,
    ".md": "myst_parser.parsers.myst",
}

# -- Coverage extension configuration ----------------------------------------

# Coverage options
coverage_show_missing_items = True
coverage_skip_undoc_in_source = False
coverage_write_headline = True

# What to check for coverage
coverage_ignore_modules = [
    "nostr_tools._version",
]

coverage_ignore_functions = [
    "__repr__",
    "__str__",
    "__eq__",
    "__hash__",
]

# -- Autodoc configuration ---------------------------------------------------

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}

autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"
autodoc_class_signature = "mixed"

# -- Autosummary configuration -----------------------------------------------

# Generate stubs automatically
autosummary_generate = True
autosummary_imported_members = False
autosummary_generate_overwrite = True

# MyST settings (Markdown parser)
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# Intersphinx settings (links to other docs)
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "aiohttp": ("https://docs.aiohttp.org/en/stable/", None),
    "websockets": ("https://websockets.readthedocs.io/en/stable/", None),
}

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_title = f"{project} v{version}"
html_short_title = project

# No custom static files - let the theme handle everything
html_static_path = []

# Furo theme options
html_theme_options = {
    # Navigation
    "navigation_with_keys": True,
    # Sidebar
    "sidebar_hide_name": False,
    # Footer
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/bigbrotr/nostr-tools",
            "html": '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>',
        },
    ],
}

# -- Options for LaTeX output ------------------------------------------------
latex_engine = "pdflatex"
latex_elements = {
    "papersize": "letterpaper",
    "pointsize": "10pt",
    "preamble": "",
    "fncychap": "\\usepackage[Bjornstrup]{fncychap}",
    "printindex": "\\footnotesize\\raggedright\\printindex",
}

latex_documents = [
    (
        "index",
        "nostr-tools.tex",
        f"{project} Documentation",
        author,
        "manual",
    ),
]

# -- Options for manual page output ------------------------------------------
man_pages = [("index", "nostr-tools", f"{project} Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    (
        "index",
        "nostr-tools",
        f"{project} Documentation",
        author,
        "nostr-tools",
        "A comprehensive Python library for Nostr protocol interactions",
        "Miscellaneous",
    ),
]

# -- Options for Epub output -------------------------------------------------
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
