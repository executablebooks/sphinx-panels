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

DEFAULT_CONTAINER = "container pb-4"
DEFAULT_COLUMN = "col-lg-6 col-md-6 col-sm-6 col-xs-12"
DEFAULT_CARD = "shadow"

RE_OPTIONS = re.compile(
    r"(column|card|body|header|footer|"
    r"img-top|img-bottom|img-top-cls|img-bottom-cls)\s*(\+?=)\s*(.*)"
)

LOCAL_FOLDER = os.path.dirname(os.path.abspath(__file__))


def parse_panels(
    content,
    content_offset,
    default_classes,
    panel_char=".",
    head_char="^",
    foot_char="+",
):
    """split a block of content into panels.

    - each panel is split by ``---``
    - an initial ``---`` before the first panel is optional
    - within each panel, the content can be further split into a header (before ``===``)
      and footer (after ``...``)

    example::

        ---
        header
        ===
        body
        ...
        footer
        ---
        next panel

    """
    if isinstance(content, str):
        content = content.splitlines()

    panel_blocks = []
    start_line = 0
    header_split = footer_split = None
    for i, line in enumerate(content):
        if line.startswith(panel_char * 3):
            if i != 0:
                panel_blocks.append(
                    parse_single_panel(
                        content[start_line:i],
                        start_line,
                        header_split,
                        footer_split,
                        content_offset,
                        default_classes,
                    )
                )
            start_line = i + 1
            header_split = footer_split = None
        if line.startswith(head_char * 3) and footer_split is None:
            header_split = i - start_line
        if line.startswith(foot_char * 3):
            footer_split = i - start_line
        # TODO warn if multiple header_split or footer_split
        # TODO assert header_split is before footer_split
    try:
        panel_blocks.append(
            parse_single_panel(
                content[start_line:],
                start_line,
                header_split,
                footer_split,
                content_offset,
                default_classes,
            )
        )
    except IndexError:
        pass
    return panel_blocks


def parse_single_panel(
    content, offset, header_split, footer_split, content_offset, default_classes
):
    """parse each panel data to dict."""
    output = {}
    body_start = 0
    body_end = len(content)

    # parse the classes required for this panel, and top/bottom images
    classes = default_classes.copy()
    for opt_offset, line in enumerate(content):
        opt_match = RE_OPTIONS.match(line)
        if not opt_match:
            break
        body_start += 1
        if opt_match.group(1) in ["img-top", "img-bottom"]:
            output[opt_match.group(1)] = opt_match.group(3)
            continue
        if opt_match.group(2) == "+=":
            classes[opt_match.group(1)] = (
                classes.get(opt_match.group(1), []) + opt_match.group(3).split()
            )
        else:
            classes[opt_match.group(1)] = opt_match.group(3).split()

    if classes:
        output["classes"] = classes

    if header_split is not None:
        header_content = content[opt_offset:header_split]
        header_offset = content_offset + offset + opt_offset
        body_start = header_split + 1
        output["header"] = (header_content, header_offset)

    if footer_split is not None:
        footer_content = content[footer_split + 1 :]
        footer_offset = content_offset + offset + footer_split
        body_end = footer_split
        output["footer"] = (footer_content, footer_offset)

    body_content = content[body_start:body_end]
    body_offset = content_offset + offset + body_start
    output["body"] = (body_content, body_offset)
    return output


def add_child_classes(node):
    """Add classes to specific child nodes."""
    for para in node.traverse(nodes.paragraph):
        para["classes"] = ([] if "classes" in para else para["classes"]) + ["card-text"]
    for title in node.traverse(nodes.title):
        title["classes"] = ([] if "classes" in title else title["classes"]) + [
            "card-title"
        ]


class Panels(SphinxDirective):
    """Two Column Panels."""

    has_content = True
    option_spec = {
        "container": directives.unchanged,
        "column": directives.unchanged,
        "card": directives.unchanged,
        "body": directives.unchanged,
        "header": directives.unchanged,
        "footer": directives.unchanged,
        "img-top-cls": directives.unchanged,
        "img-bottom-cls": directives.unchanged,
    }

    def run(self):

        container_classes = self.options.get("container", DEFAULT_CONTAINER).split()
        default_classes = {
            "column": self.options.get("column", DEFAULT_COLUMN).split(),
            "card": self.options.get("card", DEFAULT_CARD).split(),
            "body": self.options.get("body", "").split(),
            "header": self.options.get("header", "").split(),
            "footer": self.options.get("footer", "").split(),
            "img-top-cls": self.options.get("img-top-cls", "").split(),
            "img-bottom-cls": self.options.get("img-bottom-cls", "").split(),
        }

        # split the block into panels
        panel_blocks = parse_panels(
            self.content,
            self.content_offset,
            default_classes,
            panel_char=self.env.app.config.panels_delimiters[0],
            head_char=self.env.app.config.panels_delimiters[1],
            foot_char=self.env.app.config.panels_delimiters[2],
        )

        # set the top-level containers
        parent = nodes.container(in_panel=True, classes=container_classes)
        rows = nodes.container(in_panel=True, classes=["row"])
        parent += rows

        for data in panel_blocks:

            classes = data["classes"]

            column = nodes.container(
                in_panel=True, classes=["d-flex"] + classes["column"]
            )
            rows += column
            card = nodes.container(
                in_panel=True, classes=["card", "w-100"] + classes["card"]
            )
            column += card

            if "img-top" in data:
                image_top = nodes.image(
                    "",
                    uri=directives.uri(data["img-top"]),
                    alt="img-top",
                    classes=["card-img-top"] + classes["img-top-cls"],
                )
                self.add_name(image_top)
                card += image_top

            if "header" in data:
                header = nodes.container(
                    in_panel=True, classes=["card-header"] + classes["header"]
                )
                card += header

                header_content, header_offset = data["header"]
                self.state.nested_parse(header_content, header_offset, header)
                add_child_classes(header)

            body = nodes.container(
                in_panel=True, classes=["card-body"] + classes["body"]
            )
            card += body

            body_content, body_offset = data["body"]
            self.state.nested_parse(body_content, body_offset, body)
            add_child_classes(body)

            if "footer" in data:
                footer = nodes.container(
                    in_panel=True, classes=["card-footer"] + classes["footer"]
                )
                card += footer

                footer_content, footer_offset = data["footer"]
                self.state.nested_parse(footer_content, footer_offset, footer)
                add_child_classes(footer)

            if "img-bottom" in data:
                image_top = nodes.image(
                    "",
                    uri=directives.uri(data["img-bottom"]),
                    alt="img-bottom",
                    classes=["card-img-bottom"] + classes["img-bottom-cls"],
                )
                self.add_name(image_top)
                card += image_top

        return [parent]


def validate_config(app, config):
    if len(app.config.panels_delimiters) != 3:
        raise AssertionError(
            "panels_delimiters config must be of form: (header, body, footer)"
        )
    if len(set(app.config.panels_delimiters)) != 3:
        raise AssertionError("panels_delimiters config must contain unique values")
    for delim in app.config.panels_delimiters:
        if not (isinstance(delim, str) and len(delim) == 1):
            raise AssertionError(
                "panels_delimiters config must contain only length 1 strings"
            )


def add_static_paths(app):
    if app.config.panels_add_boostrap_css:
        app.config.html_static_path.append(os.path.join(LOCAL_FOLDER, "css"))
        app.add_css_file("bs-grids.css")
        app.add_css_file("bs-cards.css")
        app.add_css_file("bs-borders.css")


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
    app.add_config_value("panels_delimiters", (".", "^", "+"), "env")
    app.connect("config-inited", validate_config)
    app.add_config_value("panels_add_boostrap_css", True, "env")
    app.connect("builder-inited", add_static_paths)
    # we override container html visitors,
    # to stop the default behaviour of adding the `container` class to all nodes
    app.add_node(
        nodes.container, override=True, html=(visit_container, depart_container)
    )

    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
