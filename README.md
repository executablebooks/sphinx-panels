# sphinx-panels

[![Doc Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]
[![PyPI][pypi-badge]][pypi-link]

A sphinx extension for creating document components optimised for HTML+CSS.

- The `panels` directive creates panels of content in a grid layout, utilising both the Bootstrap 4 [grid system](https://getbootstrap.com/docs/4.0/layout/grid/), and [cards layout](https://getbootstrap.com/docs/4.0/components/card/).

- The `link-button` directive creates a click-able button, linking to a URL or reference, and can also be used to make an entire panel click-able.

- The `dropdown` directive creates toggle-able content.

- The `tabbed` directive creates tabbed content.

- `opticon` and `fa` (fontawesome) roles allow for inline icons to be added.


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

## Development

To run the tests:

```console
pip install tox
tox -e py37-sphinx3
```

To test building the docs:

```console
tox -e docs-clean html
tox -e docs-rebuild html
```

For live builds of the docs:

```console
tox -e docs-live html
```

You can also build the docs in different themes, by setting `HTML_THEME` to one of `alabaster`, `sphinx_rtd_theme`, `pydata_sphinx_theme`, `sphinx_book_theme`:

```console
export HTML_THEME=sphinx_book_theme
tox -e docs-live
```

For code style and SCSS -> CSS updating:

```console
pip install pre-commit
pre-commit run --all
```

[rtd-badge]: https://readthedocs.org/projects/sphinx-panels/badge/?version=latest
[rtd-link]: https://sphinx-panels.readthedocs.io/en/latest/?badge=latest
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/ambv/black
[pypi-badge]: https://img.shields.io/pypi/v/sphinx-panels.svg
[pypi-link]: https://pypi.org/project/sphinx-panels
