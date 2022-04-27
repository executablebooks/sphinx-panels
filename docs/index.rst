.. _panels/usage:

=============
sphinx-panels
=============

.. warning::

   This repository is not actively maintained.
   Use `sphinx-design <https://github.com/executablebooks/sphinx-design>`_ instead!
   See `the migration guide <https://sphinx-design.readthedocs.io/en/latest/get_started.html#migrating-from-sphinx-panels>`_ and `this github issue <https://github.com/executablebooks/sphinx-design/issues/51>`_ for more information.

A sphinx extension for creating panels in a grid layout or as drop-downs.

- The ``panels`` directive creates panels of content in a grid layout, utilising both the bootstrap 4
  `grid system <https://getbootstrap.com/docs/4.0/layout/grid/>`_,
  and `cards layout <https://getbootstrap.com/docs/4.0/components/card/>`_.
- The ``link-button`` directive creates a click-able button, linking to a URL or reference,
  and can also be used to make an entire panel click-able.
- The ``dropdown`` directive creates toggle-able content.
- The ``tabbed`` directive creates tabbed content.
- ``opticon`` and ``fa`` roles allow for inline icons to be added.

.. tabbed:: ReStructuredText

    .. code-block:: rst

        .. panels::

            Content of the top-left panel

            ---

            Content of the top-right panel

            :badge:`example,badge-primary`

            ---

            .. dropdown:: :fa:`eye,mr-1` Bottom-left panel

                Hidden content

            ---

            .. link-button:: https://example.com
                :text: Clickable Panel
                :classes: stretched-link

.. tabbed:: MyST Markdown

    .. code-block:: md

        ````{panels}
        Content of the top-left panel

        ---

        Content of the top-right panel

        {badge}`example,badge-primary`

        ---

        ```{dropdown} :fa:`eye,mr-1` Bottom-left panel
        Hidden content
        ```

        ---

        ```{link-button} https://example.com
        :text: Clickable Panel
        :classes: stretched-link
        ```

        ````

.. panels::

    Content of the top-left panel

    ---

    Content of the top-right panel

    :badge:`example,badge-primary`

    ---

    .. dropdown:: :fa:`eye,mr-1` Bottom-left panel

        Hidden content

    ---

    .. link-button:: https://example.com
        :text: Clickable Panel
        :classes: stretched-link

.. dropdown:: :fa:`eye,mr-1` See this documentation in other themes
    :title: text-info font-weight-bold

    Click the links to see the documentation built with:

    - `alabaster <https://sphinx-panels.readthedocs.io/en/alabaster-theme/>`_
    - `sphinx-rtd-theme <https://sphinx-panels.readthedocs.io>`_
    - `sphinx-pydata-theme <https://sphinx-panels.readthedocs.io/en/pydata-theme/>`_
    - `sphinx-book-theme <https://sphinx-panels.readthedocs.io/en/sphinx-book-theme/>`_


.. panels::
    :column: col-lg-12 p-0
    :header: text-secondary font-weight-bold

    :fa:`arrows-alt,mr-1` Adaptive Sizing

    ^^^

    Try shrinking the size of this window,
    to see how the panels above realign to compensate for small screens.

.. contents::
    :local:
    :depth: 2

Installation
============

You can install ``sphinx-panels`` with ``pip``:

.. code-block:: bash

    pip install sphinx-panels

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

This extension includes the bootstrap 4 CSS classes relevant to panels and loads it by default.
However if you already load your own Bootstrap CSS (e.g., if your theme loads it already), you may choose *not* to add it with ``sphinx-panels``.
To do so, use the following configuration in ``conf.py``:

.. code-block:: python

   panels_add_bootstrap_css = False

You can also change the delimiter regexes used by adding ``panel_delimiters`` to your ``conf.py``,
e.g. the default value (panels, header, footer) is:

.. code-block:: python

    panels_delimiters = (r"^\-{3,}$", r"^\^{3,}$", r"^\+{3,}$")

.. _components-panels:

Panels Usage
============

Grid Layout
-----------

Panels are split by three or more ``-`` characters.
The layout of panels is then set by using the bootstrap classes.
Default classes for all panels may be set in the directive options,
then panel specific classes can be added at the start of each panel.

By default the new classes will override those set previously
(as defaults or in the top level options),
but starting the option value with ``+`` will make the classes additive.
For example the following options will set the first panel's card to have both the ``shadow`` and ``bg-info`` classes:

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
split by three or more ``^^^`` and ``+++`` respectively.

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

- `Card colouring <https://getbootstrap.com/docs/4.0/utilities/colors/>`_  contextual classes: ``bg-primary``, ``bg-success``, ``bg-info``, ``bg-warning``, ``bg-danger``, ``bg-secondary`, ``bg-dark`` and ``bg-light``.
- `Padding and margins <https://getbootstrap.com/docs/4.0/utilities/spacing/>`_: ``border-0``, ``p-2``, ``m-2``, ---
- `Text alignment <https://getbootstrap.com/docs/4.0/utilities/text/#text-alignment>`_: ``text-justify``, ``text-left``, ``text-center``, ``text-right``

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

.. _components-buttons:

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

.. _components-badges:

Link Badges
===========

Badges are inline text with special formatting. Use the ``badge`` role to assign
`Bootstrap badge formatting <https://getbootstrap.com/docs/4.0/components/badge/>`_.
Text and classes are delimited by a comma:

.. code-block:: rst

    :badge:`primary,badge-primary`

    :badge:`primary,badge-primary badge-pill`

:badge:`primary,badge-primary`
:badge:`secondary,badge-secondary`
:badge:`info,badge-info`
:badge:`success,badge-success`
:badge:`danger,badge-danger`
:badge:`warning,badge-warning`
:badge:`light,badge-light`
:badge:`dark,badge-dark`

:badge:`primary,badge-primary badge-pill`
:badge:`secondary,badge-secondary badge-pill`
:badge:`info,badge-info badge-pill`
:badge:`success,badge-success badge-pill`
:badge:`danger,badge-danger badge-pill`
:badge:`warning,badge-warning badge-pill`
:badge:`light,badge-light badge-pill`
:badge:`dark,badge-dark badge-pill`

The ``link-badge`` also adds the ability to use a link to a URI or reference:

.. code-block:: rst

    :link-badge:`https://example.com,cls=badge-primary text-white,tooltip=a tooltip`
    :link-badge:`https://example.com,"my, text",cls=badge-dark text-white`
    :link-badge:`panels/usage,my reference,ref,badge-success text-white,hallo`

:link-badge:`https://example.com,cls=badge-primary text-white,tooltip=a tooltip`
:link-badge:`https://example.com,"my, text",cls=badge-dark text-white`
:link-badge:`panels/usage,my reference,ref,badge-success text-white`

Note the inputs are parsed by the following functions. The role text therefore uses these
function signatures, except you don't need to use quoted strings,
unless the string contains a comma.

.. code-block:: python

    def get_badge_inputs(text, cls: str = ""):
        return text, cls.split()

    def get_link_badge_inputs(link, text=None, type="link", cls: str = "", tooltip=None):
        return link, text or link, type, cls.split(), tooltip

.. _components-dropdown:

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

If the drop-down has no title assigned, it will display an ellipsis, which is hidden when open:

.. code-block:: rst

    .. dropdown::

        My Content

.. dropdown::

    My Content

The overarching container, title banner and body panel can all be styled by assigning classes.
Adding ``+`` at the start appends the classes to any default ones.

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

Adding the ``animate`` option will trigger an animation when the content of the drop-down is opened.

.. code-block:: rst

    .. dropdown:: My content will fade in
        :animate: fade-in

        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

.. dropdown:: My content will fade in
    :animate: fade-in

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

.. dropdown:: My content will fade in and slide down
    :animate: fade-in-slide-down

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

.. note::

    Current available inputs: ``fade-in``, ``fade-in-slide-down``

.. _components-tabbed:

Tabbed Content
==============

The ``tabbed`` directive generates tabbed selection panels.

Sequential directives will be grouped together, unless the ``:new-group`` option is added.
You can set which tab will be shown by default, using the ``:selected:`` option.

Tab directives can contain any content, and you can also set CSS classes with ``:class-label:`` and ``:class-content:``:

.. code-block:: rst

    .. tabbed:: Tab 1

        Tab 1 content

    .. tabbed:: Tab 2
        :class-content: pl-1 bg-primary

        Tab 2 content

    .. tabbed:: Tab 3
        :new-group:

        .. code-block:: python

            import pip

    .. tabbed:: Tab 4
        :selected:

        .. dropdown:: Nested Dropdown

            Some content

.. tabbed:: Tab 1

    Tab 1 content

.. tabbed:: Tab 2
    :class-content: pl-1 bg-primary

    Tab 2 content

.. tabbed:: Tab 3
    :new-group:

    .. code-block:: python

        import pip

.. tabbed:: Tab 4
    :selected:

    .. dropdown:: Nested Dropdown

        Some content

Here's an example of showing an example in multiple programming languages:

.. tabbed:: c++

    .. code-block:: c++

        int main(const int argc, const char **argv) {
          return 0;
        }

.. tabbed:: python

    .. code-block:: python

        def main():
            return

.. tabbed:: java

    .. code-block:: java

        class Main {
            public static void main(String[] args) {
            }
        }

.. tabbed:: julia

    .. code-block:: julia

        function main()
        end

.. tabbed:: fortran

    .. code-block:: fortran

        PROGRAM main
        END PROGRAM main

You can also control the colors of the labels and lines, setting ``panels_css_variables`` in your ``conf.py``.
Here are the defaults:

.. code-block:: python

    panels_css_variables = {
        "tabs-color-label-active": "hsla(231, 99%, 66%, 1)",
        "tabs-color-label-inactive": "rgba(178, 206, 245, 0.62)",
        "tabs-color-overline": "rgb(207, 236, 238)",
        "tabs-color-underline": "rgb(207, 236, 238)",
        "tabs-size-label": "1rem",
    }

.. seealso::

    Note, the `sphinx-tabs <https://github.com/executablebooks/sphinx-tabs>`__ package also offers directives to create tabs.
    The key difference is that, whereas ``sphinx-tabs`` uses JavaScript to implement this functionality, ``sphinx-panels`` only uses CSS.
    A CSS only solution has the benefit of faster load-times, and working when JS is disabled, although JS allows ``sphinx-tabs`` to implement some extended functionality (like synchronized selections).

.. _components-icons:

Inline Icons
============

Inline icons can be added to your text from either the
`GitHub octicon <https://octicons-git-v2.primer.now.sh/octicons/>`_ or
`FontAwesome <https://fontawesome.com/icons?d=gallery&m=free>`_ libraries.

====================================================== ===============================================
rST                                                    Output
====================================================== ===============================================
``:opticon:`report```                                  :opticon:`report`
``:opticon:`x-circle,text-white bg-danger,size=24```   :opticon:`x-circle,text-white bg-danger,size=24`
``:fa:`save```                                         :fa:`save`
``:fa:`spinner,text-white bg-primary fa-2x,style=fa``` :fa:`spinner,text-white bg-primary fa-2x,style=fa`
====================================================== ===============================================

Note that the theme you are using does not already include the FontAwesome CSS,
it should be loaded in your ``conf.py``,
with the `html_css_files <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_css_files>`_ option, e.g.:

.. code-block:: python

    html_css_files = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"]

By default, icons will only be output in HTML formats.
But if you want fontawesome icons to be output on LaTeX, using the `fontawesome package <https://ctan.org/pkg/fontawesome>`_,
you can add to your ``conf.py``:

.. code-block:: python

    panels_add_fontawesome_latex = True

Additional classes can be added after a comma delimiter.
Also the size (16px or 24px) can be set for opticons, and the style/prefix for fontawesome (version 5).

.. seealso::

    https://www.w3schools.com/icons/fontawesome_icons_intro.asp

.. _components-div:

Div Directive
=============

The ``div`` directive is the same as the `container directive <https://docutils.sourceforge.io/docs/ref/rst/directives.html#container>`_,
but does not add a ``container`` class in HTML outputs, which is incompatible with Bootstrap CSS:

.. code-block:: rst

    .. div:: text-primary

        hallo

.. div:: text-primary

    hallo


Combined Example
================

.. code-block:: rst

    .. dropdown:: Panels in a drop-down
        :title: bg-success text-warning
        :open:
        :animate: fade-in-slide-down

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
    :title: bg-success text-warning
    :open:
    :animate: fade-in-slide-down

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
