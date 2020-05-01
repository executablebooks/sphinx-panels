=============
sphinx-panels
=============

A sphinx extension for creating panels in a grid layout.

This directive creates panels of content in a 2 x N layout.
The panels are separated by three or more ``-``

.. code-block:: rst

    .. panels::
        :centred:

        Content of the top-left panel

        ---

        Content of the top-right panel

        ---

        Content of the bottom-left panel

        ---

        Content of the bottom-right panel


.. panels::
    :centred:

    Content of the top-left panel

    ---

    Content of the top-right panel

    ---

    Content of the bottom-left panel

    ---

    Content of the bottom-right panel


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
