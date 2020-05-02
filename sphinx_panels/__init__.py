""""A small sphinx extension to add a ``panels`` directive.

This directive creates panels of content in a 2 x N layout.
The panels are separated by `---`::

    .. panels::
        :centred:

        Content of the top-left panel

        ---

        Content of the top-right panel

        ---

        Content of the bottom-left panel

        ---

        Content of the bottom-right panel

The content can be any valid rST.
`:centred:` indicates that the panel contents should be horizontally centred.
"""
import os
import re
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective

__version__ = "0.2.0"

DEFAULT_CONTAINER = "container pad-bottom-20"
DEFAULT_COLUMN = "col-lg-6 col-md-6 col-sm-6 col-xs-12"
DEFAULT_CARD = "shadow"

RE_OPTIONS = re.compile(r"(column|card|body|title|footer)\s*(\+?=)\s*(.*)")


class Panels(SphinxDirective):
    """Two Column Panels."""

    has_content = True
    option_spec = {
        "container": directives.unchanged,
        "column": directives.unchanged,
        "card": directives.unchanged,
        "body": directives.unchanged,
        "title": directives.unchanged,
        "footer": directives.unchanged,
    }

    def run(self):

        container_classes = self.options.get("container", DEFAULT_CONTAINER).split()
        default_classes = {
            "column": self.options.get("column", DEFAULT_COLUMN).split(),
            "card": self.options.get("card", DEFAULT_CARD).split(),
            "body": self.options.get("body", "").split(),
            "title": self.options.get("title", "").split(),
            "footer": self.options.get("footer", "").split(),
        }

        # split the block into panels
        panel_blocks = []
        start_line = 0
        header_split = footer_split = None
        for i, line in enumerate(self.content):
            if line.startswith("---"):
                if i != 0:
                    panel_blocks.append(
                        (
                            self.content[start_line:i],
                            start_line,
                            header_split,
                            footer_split,
                        )
                    )
                start_line = i + 1
                header_split = footer_split = None
            if line.startswith("==="):
                header_split = i - start_line
            if line.startswith("..."):
                footer_split = i - start_line
            # TODO warn if header_split or footer_split not None
        try:
            panel_blocks.append(
                (self.content[start_line:], start_line, header_split, footer_split)
            )
        except IndexError:
            pass

        parent = nodes.container(in_panel=True, classes=container_classes)
        rows = nodes.container(in_panel=True, classes=["row"])
        parent += rows

        for (content, offset, header_split, footer_split) in panel_blocks:
            classes = default_classes.copy()
            for opt_offset, line in enumerate(content):
                opt_match = RE_OPTIONS.match(line)
                if not opt_match:
                    break
                if opt_match.group(2) == "+=":
                    classes[opt_match.group(1)] = (
                        classes[opt_match.group(1)] + opt_match.group(3).split()
                    )
                else:
                    classes[opt_match.group(1)] = opt_match.group(3).split()

            body_start = opt_offset
            body_end = len(content)

            if header_split is not None:
                title_content = content[opt_offset:header_split]
                title_offset = self.content_offset + offset + opt_offset
                body_start = header_split + 1
            else:
                title_content = False

            if footer_split is not None:
                footer_content = content[footer_split + 1 :]
                footer_offset = self.content_offset + offset + footer_split
                body_end = footer_split
            else:
                footer_content = False

            body_content = content[body_start:body_end]
            body_offset = self.content_offset + offset + body_start

            column = nodes.container(
                in_panel=True, classes=["d-flex"] + classes["column"]
            )
            rows += column
            card = nodes.container(
                in_panel=True, classes=["card", "w-100", "panel-card"] + classes["card"]
            )
            column += card

            if title_content:
                title = nodes.container(
                    in_panel=True, classes=["card-title"] + classes["title"]
                )
                card += title
                self.state.nested_parse(title_content, title_offset, title)

            body = nodes.container(
                in_panel=True, classes=["card-body"] + classes["body"]
            )
            card += body
            self.state.nested_parse(body_content, body_offset, body)

            if footer_content:
                footer = nodes.container(
                    in_panel=True, classes=["card-footer"] + classes["footer"]
                )
                card += footer
                self.state.nested_parse(footer_content, footer_offset, footer)

        return [parent]


def add_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "_static"))
    if static_path not in app.config.html_static_path:
        app.config.html_static_path.append(static_path)


def visit_container(self, node):
    classes = "docutils container"
    if node.get("in_panel", False):
        # we don't want the CSS for container for these nodes
        classes = "docutils"
    self.body.append(self.starttag(node, "div", CLASS=classes))


def depart_container(self, node):
    self.body.append("</div>\n")


def setup(app):
    app.add_directive("panels", Panels)
    app.connect("builder-inited", add_static_path)

    app.add_css_file("panels.css")

    # TODO only load these is using a non-boostrap theme
    app.add_css_file("bs-grids.css")
    app.add_css_file("bs-cards.css")

    # we override container html visitors,
    # to stop the default behaviour of adding the `container` class to all nodes
    app.add_node(
        nodes.container, override=True, html=(visit_container, depart_container)
    )

    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
