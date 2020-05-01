# sphinx-panels

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
