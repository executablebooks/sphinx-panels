""""A sphinx extension to add a ``panels`` directive."""
from pathlib import Path

try:
    import importlib.resources as resources
except ImportError:
    # python < 3.7
    import importlib_resources as resources

from docutils import nodes
from docutils.parsers.rst import directives, Directive
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util.logging import getLogger

from .button import setup_link_button
from .dropdown import setup_dropdown
from .panels import setup_panels
from .icons import setup_icons

from ._css import panels as css_panels
from ._css import bootstrap as css_bootstrap

__version__ = "0.4.1"

LOGGER = getLogger(__name__)


def compile_scss(app: Sphinx):
    """Compile SCSS to the build directory."""
    # reset css changed attribute
    app.env.panels_css_changed = False

    # setup up new static path in output dir
    static_path = (Path(app.outdir) / "_panels_static").absolute()
    static_path.mkdir(exist_ok=True)
    app.config.html_static_path.append(str(static_path))

    existing_names = {path.name for path in static_path.glob("*") if path.is_file()}

    css_resources = [("spanels-", css_panels)]
    if app.config.panels_add_boostrap_css:
        css_resources.append(("spanels-bootstrap-", css_bootstrap))

    # add new resources
    for prefix, module in css_resources:
        for filename in resources.contents(module):
            if not filename.endswith(".css"):
                continue
            out_name = prefix + filename
            if not (static_path / out_name).exists():
                content = resources.read_text(module, filename)
                (static_path / out_name).write_text(content)
                app.env.panels_css_changed = True
            app.add_css_file(prefix + filename)
            if prefix + filename in existing_names:
                existing_names.remove(prefix + filename)

    # remove old resources
    for name in existing_names:
        for path in Path(app.outdir).glob(f"**/{name}"):
            path.unlink()


def update_css_links(app: Sphinx, env: BuildEnvironment):
    """If CSS has changed, all files must be re-written,
    to include the correct stylesheets.
    """
    if env.panels_css_changed and app.config.panels_dev_mode:
        LOGGER.debug("sphinx-panels CSS changed; re-writing all files")
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
    app.add_config_value("panels_dev_mode", False, "env")
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
