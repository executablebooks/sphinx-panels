""""A sphinx extension to add a ``panels`` directive."""
import hashlib
from pathlib import Path

from docutils import nodes
from docutils.parsers.rst import directives, Directive
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from scss.compiler import compile_file

from .button import setup_link_button
from .dropdown import setup_dropdown
from .panels import setup_panels
from .icons import setup_icons

__version__ = "0.4.1"


def compile_scss(app: Sphinx):
    """Compile SCSS to the build directory."""
    # reset css changed attribute
    app.env.panels_css_changed = False

    # setup up new static path in output dir
    static_path = (Path(app.outdir) / "_panels_static").absolute()
    static_path.mkdir(exist_ok=True)
    app.config.html_static_path.append(str(static_path))

    # set sass files to compile
    sass_path = Path(__file__).parent.joinpath("scss").absolute()
    sass_files = {"sphinx-panels-dropdown": sass_path / "dropdown" / "index.scss"}
    if app.config.panels_add_boostrap_css:
        sass_files["sphinx-panels-bootstrap"] = sass_path / "bootstrap" / "index.scss"

    for name, path in sass_files.items():
        # get the string and hash of the css
        css_string_out = compile_file(str(path), output_style="compressed")
        hashstring = hashlib.md5(css_string_out.encode("utf8")).hexdigest()
        css_name = f"{name}.{hashstring}.css"
        if not (static_path / css_name).exists():
            # remove any old hashes for re-builds
            for old_path in Path(app.outdir).glob(f"**/{name}.*.css"):
                old_path.unlink()
            # write the file
            (static_path / css_name).write_text(css_string_out, encoding="utf8")
            # note that css has changed
            app.env.panels_css_changed = True
        app.add_css_file(css_name)


def update_css_links(app: Sphinx, env: BuildEnvironment):
    """If CSS has changed, all files must be re-written,
    to include the correct stylesheets.
    """
    # note, ideally here we would only do this for html builders
    # but this is actually quite hard to identify, since the builder name doesn't
    # always include 'html' (e.g. readthedocs)
    if env.panels_css_changed:
        return list(env.all_docs.keys())


class Div(Directive):
    """Same as the ``container`` directive,
    but does not add the ``container`` class in HTML outputs,
    which can interfere with Bootstrap CSS.
    """

    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {"name": directives.unchanged}
    has_content = True

    def run(self):
        self.assert_has_content()
        text = "\n".join(self.content)
        try:
            if self.arguments:
                classes = directives.class_option(self.arguments[0])
            else:
                classes = []
        except ValueError:
            raise self.error(
                'Invalid class attribute value for "%s" directive: "%s".'
                % (self.name, self.arguments[0])
            )
        node = nodes.container(text, is_div=True)
        node["classes"].extend(classes)
        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


def visit_container(self, node: nodes.Node):
    classes = "docutils container"
    if node.get("is_div", False):
        # we don't want the CSS for container for these nodes
        classes = "docutils"
    self.body.append(self.starttag(node, "div", CLASS=classes))


def depart_container(self, node: nodes.Node):
    self.body.append("</div>\n")


def setup(app: Sphinx):
    app.add_directive("div", Div)
    app.add_config_value("panels_add_boostrap_css", True, "env")
    app.connect("builder-inited", compile_scss)
    app.connect("env-updated", update_css_links)
    # we override container html visitors, to stop the default behaviour
    # of adding the `container` class to all nodes.container
    app.add_node(
        nodes.container, override=True, html=(visit_container, depart_container)
    )

    setup_panels(app)
    setup_link_button(app)
    setup_dropdown(app)
    setup_icons(app)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
