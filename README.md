# sphinx-panels

[![Documentation Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]
[![PyPI][pypi-badge]][pypi-link]

A sphinx extension for creating panels in a grid layout.

This directive creates panels of content in a 2 x N layout.
The panels are separated by three or more ``-``

```rst
.. panels::
    :centred:

    Content of the top-left panel

    ---

    Content of the top-right panel

    ---

    Content of the bottom-left panel

    ---

    Content of the bottom-right panel
```

[rtd-badge]: https://readthedocs.org/projects/sphinx-panels/badge/?version=latest
[rtd-link]: https://sphinx-panels.readthedocs.io/en/latest/?badge=latest
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/ambv/black
[pypi-badge]: https://img.shields.io/pypi/v/sphinx-panels.svg
[pypi-link]: https://pypi.org/project/sphinx-panels
