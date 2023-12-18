from pathlib import Path
import shutil

import pytest
import sphinx
from sphinx.testing.path import path

from sphinx_panels.tabs import TabbedHtmlTransform


@pytest.fixture()
def sphinx_app_factory(make_app, tmp_path: Path, monkeypatch):
    monkeypatch.setattr(TabbedHtmlTransform, "get_unique_key", lambda self: "mock-uuid")

    def _func(src_folder, **kwargs):
        shutil.copytree(
            (Path(__file__).parent / "sources" / src_folder), tmp_path / src_folder
        )
        srcdir = (tmp_path / src_folder).absolute()
        if sphinx.version_info < (7, 2):
            srcdir = path(str(srcdir))
        app = make_app(srcdir=srcdir, **kwargs)
        return app

    yield _func


@pytest.mark.parametrize("folder", ["tabbed_basic", "dropdown_basic"])
def test_sources(sphinx_app_factory, file_regression, folder):
    app = sphinx_app_factory(folder)
    app.build()
    assert app._warning.getvalue() == ""
    doctree = app.env.get_and_resolve_doctree("index", app.builder)
    doctree["source"] = "source"
    if sphinx.version_info < (7, 1):
        doctree["translation_progress"] = "{'total': 0, 'translated': 0}"
    file_regression.check(
        doctree.pformat(),
        encoding="utf8",
        extension=".xml",
    )
