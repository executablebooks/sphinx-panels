# Changelog

## v0.5.0 - 2020-10-15

✨ NEW: Add `tabbed` directive, to create tab groups!
See [this documentation section](https://sphinx-panels.readthedocs.io/en/latest/#tabbed-content).

♻️ REFACTOR: Move from CSS to SCSS:
Under the hood, sphinx-panels now utilises CSS compiled from source SCSS,
allowing for a better development environment.
The CSS files are also "hashed", to ensure that documentation using sphinx-panels will not show
old, cached CSS stylings after future updates to sphinx-panels.
