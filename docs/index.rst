=============
sphinx-panels
=============

A sphinx extension for creating panels in a grid layout.

This directive creates panels of content in a grid layout,
utilising both the bootstrap 4
`grid system <https://getbootstrap.com/docs/4.0/layout/grid/>`_,
and `cards layout <https://getbootstrap.com/docs/4.0/components/card/>`_.

.. code-block:: rst

    .. panels::

        Content of the top-left panel

        ---

        Content of the top-right panel

        ---

        Content of the bottom-left panel

        ---

        Content of the bottom-right panel

.. panels::

    Content of the top-left panel

    ---

    Content of the top-right panel

    ---

    Content of the bottom-left panel

    ---

    Content of the bottom-right panel

.. tip::

    Try shrinking the size of this window,
    to see how the panels realign to compensate for small screens.


Installation
============

You can install `sphinx-panels` with `pip`:

.. code-block:: bash

    pip install sphinx-panels


Usage
=====

In your ``conf.py`` configuration file, add ``sphinx_panels``
to your extensions list, e.g.:

.. code-block:: python

    extensions = [
        ...
        'sphinx_panels'
        ...
    ]

This extension includes the bootstrap 4 CSS classes relevant to panels.
They will be loaded by default but, if you are already using a bootstrap theme,
you can disable this by adding ``add_boostrap_css = False`` to your ``conf.py``.

Detailed Examples
=================

Grid Layout
-----------

Panels are split by three or more `-` characters.
The layout of panels is then set by using the bootstrap classes.
Default classes for all panels may be set in the directive options,
then panel specific classes can be added at the start of each panel.
`=` will reset the classes, or `+=` will add to the default classes.

.. seealso::

    The bootstrap 4 `grid documentation <https://getbootstrap.com/docs/4.0/layout/grid/>`_,
    and this `grid tutorial <https://www.w3schools.com/bootstrap/bootstrap_grid_system.asp>`_

.. note::

    The default classes are:

    .. code-block:: rst

        .. panels::
            :container: container pb-4
            :column: col-lg-6 col-md-6 col-sm-6 col-xs-12
            :card: shadow

.. code-block:: rst

    .. panels::
        :container: container-lg pb-3
        :column: col-lg-4 col-md-4 col-sm-6 col-xs-12

        panel1
        ---
        panel2
        ---
        panel3
        ---
        column = col-lg-12
        panel4

.. panels::
    :container: container-lg pb-3
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12

    panel1
    ---
    panel2
    ---
    panel3
    ---
    column = col-lg-12
    panel4

Card Layout
-----------

Each panel contains a card, which can itself contain a header and/or footer,
split by three or more `=` and `.` respectively.

.. seealso::

    The bootstrap 4 `card documentation <https://getbootstrap.com/docs/4.0/components/card/>`_,
    and this `card tutorial <https://www.w3schools.com/bootstrap4/bootstrap_cards.asp>`_

.. code-block:: rst

    .. panels::

        panel 1 header
        ==============

        panel 1 content

        more content

        ..............
        panel 1 footer

        ---

        panel 2 header
        ==============

        panel 2 content

        ..............
        panel 2 footer

.. panels::

    panel 1 header
    ==============

    panel 1 content

    more content

    ..............
    panel 1 footer

    ---

    panel 2 header
    ==============

    panel 2 content

    ..............
    panel 2 footer


Card Styling
------------

To style the look of cards,
you may use the directive options to add default CSS classes for eac element,
or use the per-panel option syntax to add to or override these:

- container: the top-level container
- column: the panel container
- card: the panel card
- body: the panel card
- header: the panel header
- footer: the panel footer

You can add your own CSS (see
`the html_css_files option <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_css_files>`_)
but it is advised you use the built-in bootstrap classes:

- `Card colouring <https://getbootstrap.com/docs/4.0/utilities/colors/>`_  contextual classes: `bg-primary`, `bg-success`, `bg-info`, `bg-warning`, `bg-danger`, `bg-secondary`, `bg-dark` and `bg-light`.
- `Padding and margins <https://getbootstrap.com/docs/4.0/utilities/spacing/>`_: `border-0`, `p-2`, `m-2`, ...
- `Text alignment <https://getbootstrap.com/docs/4.0/utilities/text/#text-alignment>`_: `text-justify`, `text-left`, `text-center`, `text-right`

.. code-block:: rst

    .. panels::
        :body: bg-primary text-justify
        :header: text-center
        :footer: text-right

        ---
        column += p-1

        panel 1 header
        ==============

        panel 1 content

        ..............
        panel 1 footer

        ---
        column += p-1 text-center border-0
        body = bg-info
        header = bg-success
        footer = bg-secondary

        panel 2 header
        ==============

        panel 2 content

        ..............
        panel 2 footer

.. panels::
    :body: bg-primary text-justify
    :header: text-center
    :footer: text-right

    ---
    column += p-1

    panel 1 header
    ==============

    panel 1 content

    ..............
    panel 1 footer

    ---
    column += p-1 text-center border-0
    body = bg-info
    header = bg-success
    footer = bg-secondary

    panel 2 header
    ==============

    panel 2 content

    ..............
    panel 2 footer


Image Caps
----------

Images can be added to the top and/or bottom of the panel.
By default they will expand to fit the width of the card,
but classes can also be used to add padding:

.. code-block:: rst

    .. panels::
        :img-top-cls: pl-5 pr-5

        ---
        img-top = _static/ebp-logo.png
        img-bottom = _static/footer-banner.jpg

        header 1
        ===

        Panel 1 content

        More **content**

        ...
        tail 1

        ---
        img-top = _static/sphinx-logo.png
        img-top-cls += bg-success
        img-bottom = _static/footer-banner.jpg

        header 2
        ===

        Panel 2 content

        ...
        tail 1

.. panels::
    :img-top-cls: pl-5 pr-5
    :body: text-center

    ---
    img-top = _static/ebp-logo.png
    img-bottom = _static/footer-banner.jpg

    header 1
    ===

    Panel 1 content

    More **content**

    ...
    tail 1

    ---
    img-top = _static/sphinx-logo.png
    img-top-cls += bg-success
    img-bottom = _static/footer-banner.jpg

    header 2
    ===

    Panel 2 content

    ...
    tail 1

Additional Examples
-------------------

.. code-block:: rst

    .. panels::
        :container: container-fluid pb-3
        :column: col-lg-6 col-md-6 col-sm-12 col-xs-12 p-2
        :card: shadow
        :header: border-0
        :footer: border-0

        ---
        card += bg-warning

        header
        ======

        Content of the top-left panel

        ...

        footer

        ---
        card += bg-info
        footer += bg-danger

        header
        ======

        Content of the top-right panel

        ...

        footer

        ---
        column = col-lg-12
        card += bg-success text-center

        Content of the bottom panel


.. panels::
    :container: container-fluid pb-3
    :column: col-lg-6 col-md-6 col-sm-12 col-xs-12 p-2
    :card: shadow
    :header: border-0
    :footer: border-0

    ---
    card += bg-warning

    header
    ======

    Content of the top-left panel

    ...

    footer

    ---
    card += bg-info
    footer += bg-danger

    header
    ======

    Content of the top-right panel

    ...

    footer

    ---
    column = col-lg-12 p-3
    card += bg-success text-center

    Content of the bottom panel

Acknowledgements
================

Originally adapted from the `pandas documentation <https://pandas.pydata.org/docs/>`_.
