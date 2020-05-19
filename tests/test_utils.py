import pytest

from sphinx_panels import utils


@pytest.mark.parametrize(
    "string,expected",
    [
        ("", ([], {})),
        ("a", (["a"], {})),
        ("a,b", (["a", "b"], {})),
        ("a,1", (["a", 1], {})),
        ("1,a", ([1, "a"], {})),
        ("a,b=1", (["a"], {"b": 1})),
        ('a,b="1"', (["a"], {"b": "1"})),
        ('a , b = "1,2" ', (["a"], {"b": "1,2"})),
        ('a , b = "1,2", sdf=4 ', (["a"], {"b": "1,2", "sdf": 4})),
        ('a,b="""', (["a"], {"b": '"""'})),  # This is kind of wrong
    ],
)
def test_string_to_func_inputs(string, expected):
    assert utils.string_to_func_inputs(string) == expected
