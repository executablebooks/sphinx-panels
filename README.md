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

The `link-button` directive can be used to create buttons, which link to a URL (default) or reference.
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

The `dropdown` directive combines a [Bootstrap card](https://getbootstrap.com/docs/4.0/components/card/)
with the [HTML details tag](https://www.w3schools.com/tags/tag_details.asp) to create a collapsible
drop-down panel.

```rst
.. dropdown:: Click on me to see my content!

    I'm the content which can be anything:

    .. link-button:: https://example.com
        :text: Like a Button
        :classes: btn-primary
```

[rtd-badge]: https://readthedocs.org/projects/sphinx-panels/badge/?version=latest
[rtd-link]: https://sphinx-panels.readthedocs.io/en/latest/?badge=latest
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/ambv/black
[pypi-badge]: https://img.shields.io/pypi/v/sphinx-panels.svg
[pypi-link]: https://pypi.org/project/sphinx-panels
