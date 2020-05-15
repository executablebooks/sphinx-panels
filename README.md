# sphinx-panels

[![Doc Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]
[![PyPI][pypi-badge]][pypi-link]

A sphinx extension for creating panels in a grid layout.
utilising both the bootstrap 4
[grid system](https://getbootstrap.com/docs/4.0/layout/grid/),
and [cards layout](https://getbootstrap.com/docs/4.0/components/card/).

```rst
.. panels::

    Content of the top-left panel

    ---

    Content of the top-right panel

    ---

    Content of the bottom-left panel

    ---

    Content of the bottom-right panel
```

Also, the `link-button` directive can be used to create buttons, which link to a URL (default) or reference.
They can be styled by [Bootstrap button classes](https://getbootstrap.com/docs/4.0/components/buttons/):

```rst
.. panels::

    .. link-button:: https://example.com
        :type: url
        :tooltip: hallo
        :classes: btn-success

    ---

    This entire panel is clickable.

    +++

    .. link-button:: panels/usage
        :type: ref
        :text: Go To Reference
        :classes: btn-outline-primary btn-block stretched-link
```

[rtd-badge]: https://readthedocs.org/projects/sphinx-panels/badge/?version=latest
[rtd-link]: https://sphinx-panels.readthedocs.io/en/latest/?badge=latest
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/ambv/black
[pypi-badge]: https://img.shields.io/pypi/v/sphinx-panels.svg
[pypi-link]: https://pypi.org/project/sphinx-panels
