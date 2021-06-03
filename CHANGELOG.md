# Changelog

## v0.6.0 - 2021-06-03

⬆️ UPGRADE: Unpin sphinx v4

👌 IMPROVE: specify post-transforms by format:
This applies them to the "html" format, rathther than a subset of diretive html builders.

## v0.5.2 - 2020-10-12

‼️ Deprecate `panels_add_boostrap_css` config, the typo here (no T!) has now been fixed to `panels_add_bootstrap_css`.
Use of the former will now emit a deprecation warning.

## v0.5.1 - 2020-09-22

👌 IMPROVE: Make default label font-size configurable for `tabbed` components.
See the `panels_css_variables` [in this documentation section](https://sphinx-panels.readthedocs.io/en/latest/#tabbed-content).

## v0.5.0 - 2020-09-15

✨ NEW: Add `tabbed` directive, to create tab groups!
See [this documentation section](https://sphinx-panels.readthedocs.io/en/latest/#tabbed-content).

♻️ REFACTOR: Move from CSS to SCSS:
Under the hood, sphinx-panels now utilises CSS compiled from source SCSS,
allowing for a better development environment.
The CSS files are also "hashed", to ensure that documentation using sphinx-panels will not show
old, cached CSS stylings after future updates to sphinx-panels.
