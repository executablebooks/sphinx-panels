""""A sphinx extension to add a ``panels`` directive."""
import os

from docutils import nodes
from docutils.parsers.rst import directives, Directive

from .button import setup_link_button
from .dropdown import setup_dropdown
from .panels import setup_panels
from .icons import setup_icons

__version__ = "0.4.1"


LOCAL_FOLDER = os.path.dirname(os.path.abspath(__file__))


def add_static_paths(app):
    app.config.html_static_path.append(os.path.join(LOCAL_FOLDER, "css"))
    app.add_css_file("sphinx-dropdown.css")
    if app.config.panels_add_boostrap_css:
        app.add_css_file("panels-bootstrap.min.css")


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


def visit_container(self, node):
    classes = "docutils container"
    if node.get("is_div", False):
        # we don't want the CSS for container for these nodes
        classes = "docutils"
    self.body.append(self.starttag(node, "div", CLASS=classes))


def depart_container(self, node):
    self.body.append("</div>\n")


def setup(app):
    app.add_directive("div", Div)
    app.add_config_value("panels_add_boostrap_css", True, "env")
    app.connect("builder-inited", add_static_paths)
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
