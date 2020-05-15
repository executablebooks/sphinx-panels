import pytest

from sphinx_panels.panels import parse_panels


@pytest.mark.parametrize(
    "content,expected",
    (
        ("a", [{"body": (["a"], 0)}]),
        ("---\na", [{"body": (["a"], 1)}]),
        ("a\n^^^", [{"body": ([], 2), "header": (["a"], 0)}]),
        ("a\n+++", [{"body": (["a"], 0), "footer": ([], 1)}]),
        (
            "a\n^^^\nb\n+++\nc",
            [{"body": (["b"], 2), "footer": (["c"], 3), "header": (["a"], 0)}],
        ),
        ("---\n:card: a", [{"body": ([], 2), "classes": {"card": ["a"]}}]),
        ("a\n---\nb", [{"body": (["a"], 0)}, {"body": (["b"], 2)}]),
    ),
)
def test_parse_panels(content, expected):
    output = parse_panels(content, content_offset=0, default_classes={})
    assert output == expected
