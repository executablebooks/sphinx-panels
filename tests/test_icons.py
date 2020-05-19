from sphinx_panels import icons


def test_opticon_simple():
    string = icons.get_opticon("report")
    assert string == (
        '<svg version="1.1" width="16" height="16" class="octicon octicon-report" '
        'viewBox="0 0 16 16" aria-hidden="true">'
        '<path fill-rule="evenodd" d="M1.75 1.5a.25.25 0 00-.25.25v9.5c0 '
        ".138.112.25.25.25h2a.75.75 0 01.75.75v2.19l2.72-2.72a.75.75 "
        "0 01.53-.22h6.5a.25.25 0 00.25-.25v-9.5a.25.25 0 00-.25-.25H1.75zM0 1.75C0 "
        ".784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v9.5A1.75 1.75 0 0114.25 "
        "13H8.06l-2.573 2.573A1.457 1.457 0 013 14.543V13H1.75A1.75 1.75 0 010 "
        "11.25v-9.5zM9 9a1 1 0 11-2 0 1 1 0 012 0zm-.25-5.25a.75.75 0 00-1.5 "
        '0v2.5a.75.75 0 001.5 0v-2.5z"></path></svg>'
    )


def test_opticon_with_options():
    string = icons.get_opticon(
        "kebab-horizontal", width=36.0, size=24, classes="custom", aria_label="other"
    )
    assert string == (
        '<svg version="1.1" width="36.0" height="36.0" '
        'class="octicon octicon-kebab-horizontal custom" viewBox="0 0 36.0 36.0" '
        'aria-label="other" role="img">'
        '<path fill-rule="evenodd" d="M6 12a2 2 0 11-4 0 2 2 0 014 0zm8 0a2 2 0 11-4 '
        '0 2 2 0 014 0zm6 2a2 2 0 100-4 2 2 0 000 4z"></path></svg>'
    )
