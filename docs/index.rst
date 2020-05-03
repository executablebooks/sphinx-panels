=============
sphinx-panels
=============

A sphinx extension for creating panels in a grid layout.

This directive creates panels of content in a grid layout,
utilising both the bootstrap 4
`grid system <https://www.w3schools.com/bootstrap/bootstrap_grid_system.asp>`_,
and `cards layout <https://www.w3schools.com/bootstrap4/bootstrap_cards.asp>`_.

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
to your extensions list.

E.g.:

.. code-block:: python

    extensions = [
        ...
        'sphinx_panels'
        ...
    ]

This extension includes the bootstrap 4 CSS classes relevant to panels.
They will be loaded by default but, if you are already using a bootstrap theme,
you can disable it by adding ``add_boostrap_css = False`` to your ``conf.py``.

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

    `Bootstrap grid examples <https://getbootstrap.com/docs/4.4/examples/grid/>`_

.. code-block:: rst

    .. panels::
        :container: container-lg pad-bottom-20
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
    :container: container-lg pad-bottom-20
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

.. tip::

    For card colouring, it is advised to use the bootstrap contextual classes:
    `bg-primary`, `bg-success`, `bg-info`, `bg-warning`, `bg-danger`, `bg-secondary`, `bg-dark` and `bg-light`.

.. code-block:: rst

    .. panels::
        :card: shadow bg-primary

        panel 1 header
        ==============

        panel 1 content

        ...
        panel 1 footer

        ---
        column += text-center
        card = bg-info
        title = bg-success
        footer = bg-secondary


        panel 2 header
        ==============

        panel 2 content

        ...
        panel 2 footer

.. panels::
    :card: shadow bg-primary

    panel 1 header
    ==============

    panel 1 content

    ...
    panel 1 footer

    ---
    column += text-center
    card = bg-info
    title = bg-success
    footer = bg-secondary


    panel 2 header
    ==============

    panel 2 content

    ...
    panel 2 footer


All Features
------------

.. code-block:: rst

    .. panels::
        :container: container-fluid pad-bottom-20
        :column: col-lg-6 col-md-6 col-sm-12 col-xs-12
        :card: shadow

        ---
        card += bg-warning
        footer += bg-danger

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
        card += bg-success

        Content of the bottom panel


.. panels::
    :container: container-fluid pad-bottom-20
    :column: col-lg-6 col-md-6 col-sm-12 col-xs-12
    :card: shadow

    ---
    card += bg-warning
    footer += bg-danger

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
    card += bg-success

    Content of the bottom panel
