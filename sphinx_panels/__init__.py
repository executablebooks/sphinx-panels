""""A sphinx extension to add a ``panels`` directive."""
import os

from docutils import nodes

from .button import setup_link_button
from .dropdown import setup_dropdown
from .panels import setup_panels

__version__ = "0.4.0"


LOCAL_FOLDER = os.path.dirname(os.path.abspath(__file__))


def add_static_paths(app):
    app.config.html_static_path.append(os.path.join(LOCAL_FOLDER, "css"))
    app.add_css_file("sphinx-dropdown.css")
    if app.config.panels_add_boostrap_css:
        app.add_css_file("panels-bootstrap.min.css")


def visit_container(self, node):
    classes = "docutils container"
    if node.get("is_div", False):
        # we don't want the CSS for container for these nodes
        classes = "docutils"
    self.body.append(self.starttag(node, "div", CLASS=classes))


def depart_container(self, node):
    self.body.append("</div>\n")


def setup(app):

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

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
