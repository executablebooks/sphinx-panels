=============
sphinx-panels
=============

.. contents::
    :local:
    :depth: 2


A sphinx extension for creating panels in a grid layout or as drop-downs.

- The ``panels`` directive creates panels of content in a grid layout, utilising both the bootstrap 4
  `grid system <https://getbootstrap.com/docs/4.0/layout/grid/>`_,
  and `cards layout <https://getbootstrap.com/docs/4.0/components/card/>`_.
- The ``link-button`` directive creates a click-able button, linking to a URL or reference,
  and can also be used to make an entire panel click-able.
- The ``dropdown`` directive creates toggle-able content.

.. code-block:: rst

    .. panels::

        Content of the top-left panel

        ---

        Content of the top-right panel

        ---

        .. dropdown:: Bottom-left panel

            Hidden content

        ---

        .. link-button:: https://example.com
            :text: Clickable Panel
            :classes: stretched-link

.. panels::

    Content of the top-left panel

    ---

    Content of the top-right panel

    ---

    .. dropdown:: Bottom-left panel

        Hidden content

    ---

    .. link-button:: https://example.com
        :text: Clickable Panel
        :classes: stretched-link

.. tip::

    Try shrinking the size of this window,
    to see how the panels realign to compensate for small screens.


Installation
============

You can install `sphinx-panels` with `pip`:

.. code-block:: bash

    pip install sphinx-panels

.. _panels/usage:

Sphinx Configuration
=====================

In your ``conf.py`` configuration file, simply add ``sphinx_panels``
to your extensions list, e.g.:

.. code-block:: python

    extensions = [
        ...
        'sphinx_panels'
        ...
    ]

This extension includes the bootstrap 4 CSS classes relevant to panels.
They will be loaded by default but, if you are already using a bootstrap theme,
you can disable this by adding ``panels_add_boostrap_css = False`` to your ``conf.py``.

You can also change the delimiter regexes used by adding ``panel_delimiters`` to your ``conf.py``,
e.g. the default value (panels, header, footer) is:

.. code-block:: python

    panels_delimiters = (r"^\-{3,}$", r"^\^{3,}$", r"^\+{3,}$")


Panels Usage
============

Grid Layout
-----------

Panels are split by three or more `-` characters.
The layout of panels is then set by using the bootstrap classes.
Default classes for all panels may be set in the directive options,
then panel specific classes can be added at the start of each panel.

By default the new classes will override those set previously
(as defaults or in the top level options),
but starting the option value with `+` will make the classes additive.
For example the following options will set the first panel's card to have both the `shadow` and `bg-info` classes:

.. code-block:: rst

    .. panels::
        :card: shadow

        ---
        :card: + bg-info

.. seealso::

    The bootstrap 4 `grid documentation <https://getbootstrap.com/docs/4.0/layout/grid/>`_,
    and this `grid tutorial <https://www.w3schools.com/bootstrap/bootstrap_grid_system.asp>`_

.. note::

    The default classes are:

    .. code-block:: rst

        .. panels::
            :container: container pb-4
            :column: col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2
            :card: shadow

.. code-block:: rst

    .. panels::
        :container: container-lg pb-3
        :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2

        panel1
        ---
        panel2
        ---
        panel3
        ---
        :column: col-lg-12 p-2
        panel4

.. panels::
    :container: container-lg pb-3
    :column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2

    panel1
    ---
    panel2
    ---
    panel3
    ---
    :column: col-lg-12 p-2
    panel4

Card Layout
-----------

Each panel contains a card, which can itself contain a header and/or footer,
split by three or more `^^^` and `+++` respectively.

.. seealso::

    The bootstrap 4 `card documentation <https://getbootstrap.com/docs/4.0/components/card/>`_,
    and this `card tutorial <https://www.w3schools.com/bootstrap4/bootstrap_cards.asp>`_

.. code-block:: rst

    .. panels::

        panel 1 header
        ^^^^^^^^^^^^^^

        panel 1 content

        more content

        ++++++++++++++
        panel 1 footer

        ---

        panel 2 header
        ^^^^^^^^^^^^^^

        panel 2 content

        ++++++++++++++
        panel 2 footer

.. panels::

    panel 1 header
    ^^^^^^^^^^^^^^

    panel 1 content

    more content

    ++++++++++++++
    panel 1 footer

    ---

    panel 2 header
    ^^^^^^^^^^^^^^

    panel 2 content

    ++++++++++++++
    panel 2 footer


Card Styling
------------

To style the look of cards,
you may use the directive options to add default CSS classes for each element,
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
- `Padding and margins <https://getbootstrap.com/docs/4.0/utilities/spacing/>`_: `border-0`, `p-2`, `m-2`, ---
- `Text alignment <https://getbootstrap.com/docs/4.0/utilities/text/#text-alignment>`_: `text-justify`, `text-left`, `text-center`, `text-right`

.. code-block:: rst

    .. panels::
        :body: bg-primary text-justify
        :header: text-center
        :footer: text-right

        ---
        :column: + p-1

        panel 1 header
        ^^^^^^^^^^^^^^

        panel 1 content

        ++++++++++++++
        panel 1 footer

        ---
        :column: + p-1 text-center border-0
        :body: bg-info
        :header: bg-success
        :footer: bg-secondary

        panel 2 header
        ^^^^^^^^^^^^^^

        panel 2 content

        ++++++++++++++
        panel 2 footer

.. panels::
    :body: bg-primary text-justify
    :header: text-center
    :footer: text-right

    ---
    :column: + p-1

    panel 1 header
    ^^^^^^^^^^^^^^

    panel 1 content

    ++++++++++++++
    panel 1 footer

    ---
    :column: + p-1 text-center border-0
    :body: bg-info
    :header: bg-success
    :footer: bg-secondary

    panel 2 header
    ^^^^^^^^^^^^^^

    panel 2 content

    ++++++++++++++
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
        :img-top: _static/ebp-logo.png
        :img-bottom: _static/footer-banner.jpg

        header 1
        ^^^^^^^^

        Panel 1 content

        More **content**

        ++++++
        tail 1

        ---
        :img-top: _static/sphinx-logo.png
        :img-top-cls: + bg-success
        :img-bottom: _static/footer-banner.jpg

        header 2
        ^^^^^^^^

        Panel 2 content

        ++++++
        tail 1

.. panels::
    :img-top-cls: pl-5 pr-5
    :body: text-center

    ---
    :img-top: _static/ebp-logo.png
    :img-bottom: _static/footer-banner.jpg

    header 1
    ^^^^^^^^

    Panel 1 content

    More **content**

    ++++++
    tail 1

    ---
    :img-top: _static/sphinx-logo.png
    :img-top-cls: + bg-success
    :img-bottom: _static/footer-banner.jpg

    header 2
    ^^^^^^^^

    Panel 2 content

    ++++++
    tail 1

Link Buttons
============

The ``link-button`` directive can be used to create buttons, which link to a URL (default) or reference.
They can be styled by `Bootstrap button classes <https://getbootstrap.com/docs/4.0/components/buttons/>`_:

.. code-block:: rst

    .. link-button:: https://example.com
        :type: url
        :text: some text
        :tooltip: hallo

    .. link-button:: panels/usage
        :type: ref
        :text: some other text
        :classes: btn-outline-primary btn-block

.. link-button:: https://example.com
    :type: url
    :text: some text
    :tooltip: hallo

.. link-button:: panels/usage
    :type: ref
    :text: some other text
    :classes: btn-outline-primary btn-block

When used inside a panel, you can use the `stretched-link class <https://getbootstrap.com/docs/4.4/utilities/stretched-link/>`_,
to make the entire panel clickable:

.. code-block:: rst

    .. panels::

        .. link-button:: https://example.com
            :classes: btn-success

        ---

        This entire panel is clickable.

        +++

        .. link-button:: panels/usage
            :type: ref
            :text: Go To Reference
            :classes: btn-outline-primary btn-block stretched-link

.. panels::

    .. link-button:: https://example.com
        :classes: btn-success

    ---

    This entire panel is clickable.

    +++

    .. link-button:: panels/usage
        :type: ref
        :text: Go To Reference
        :classes: btn-outline-primary btn-block stretched-link


Dropdown Usage
==============

The ``dropdown`` directive combines a `Bootstrap card <https://getbootstrap.com/docs/4.0/components/card/>`_
with the `HTML details tag <https://www.w3schools.com/tags/tag_details.asp>`_ to create a collapsible
drop-down panel.

.. code-block:: rst

    .. dropdown:: Click on me to see my content!

        I'm the content which can be anything:

        .. link-button:: https://example.com
            :text: Like a Button
            :classes: btn-primary

.. dropdown:: Click on me to see my content!

    I'm the content which can be anything:

    .. link-button:: https://example.com
        :text: Like a Button
        :classes: btn-primary

You can start with the panel open by default using the ``open`` option:

.. code-block:: rst

    .. dropdown:: My Content
        :open:

        Is already visible

.. dropdown:: My Content
    :open:

    Is already visible

The overarching container, title banner and body panel can all be styled by assigning classes.
Adding `+` at the start appends the classes to any default ones.

.. code-block:: rst

    .. dropdown:: My Content
        :container: + shadow
        :title: bg-primary text-white text-center font-weight-bold
        :body: bg-light text-right font-italic

        Is formatted

.. dropdown:: My Content
    :container: + shadow
    :title: bg-primary text-white text-center font-weight-bold
    :body: bg-light text-right font-italic

    Is formatted

Transition Animation
--------------------

Adding the `fade-in` option will cause the content of the drop-down to fade-in when opened.

.. code-block:: rst

    .. dropdown:: My content will fade in
        :fade-in:

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

.. dropdown:: My content will fade in
    :fade-in:

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


Combined Example
================

.. code-block:: rst

    .. dropdown:: Panels in a drop-down
        :title: bg-success
        :open:
        :fade-in:

        .. panels::
            :container: container-fluid pb-1
            :column: col-lg-6 col-md-6 col-sm-12 col-xs-12 p-2
            :card: shadow
            :header: border-0
            :footer: border-0

            ---
            :card: + bg-warning

            header
            ^^^^^^

            Content of the top-left panel

            ++++++
            footer

            ---
            :card: + bg-info
            :footer: + bg-danger

            header
            ^^^^^^

            Content of the top-right panel

            ++++++
            footer

            ---
            :column: col-lg-12 p-3
            :card: + text-center

            .. link-button:: panels/usage
                :type: ref
                :text: Clickable Panel
                :classes: btn-link stretched-link font-weight-bold

.. dropdown:: Panels in a drop-down
    :title: bg-success
    :open:
    :fade-in:

    .. panels::
        :container: container-fluid pb-1
        :column: col-lg-6 col-md-6 col-sm-12 col-xs-12 p-2
        :card: shadow
        :header: border-0
        :footer: border-0

        ---
        :card: + bg-warning

        header
        ^^^^^^

        Content of the top-left panel

        ++++++
        footer

        ---
        :card: + bg-info
        :footer: + bg-danger

        header
        ^^^^^^

        Content of the top-right panel

        ++++++
        footer

        ---
        :column: col-lg-12 p-3
        :card: + text-center

        .. link-button:: panels/usage
            :type: ref
            :text: Clickable Panel
            :classes: btn-link stretched-link font-weight-bold


Acknowledgements
================

- Panels originally adapted from the `pandas documentation <https://pandas.pydata.org/docs/>`_.
- Dropdown originally adapted from `tk0miya/sphinxcontrib-details-directive  <https://github.com/tk0miya/sphinxcontrib-details-directive/>`_.
