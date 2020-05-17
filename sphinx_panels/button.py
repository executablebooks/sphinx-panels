from urllib.parse import unquote

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx import addnodes
from sphinx.util.docutils import SphinxDirective


def setup_link_button(app):
    app.add_directive("link-button", LinkButton)


class LinkButton(SphinxDirective):
    """A directive to turn a link into a button."""

    has_content = False
    required_arguments = 1
    option_spec = {
        "type": lambda arg: directives.choice(arg, ("url", "ref")),
        "text": directives.unchanged,
        "tooltip": directives.unchanged,
        "classes": directives.unchanged,
    }

    def run(self):

        uri = self.arguments[0]
        link_type = self.options.get("type", "url")

        text = self.options.get("text", uri)
        innernode = nodes.inline("", text)

        if link_type == "ref":
            ref_node = addnodes.pending_xref(
                reftarget=unquote(uri),
                reftype="any",
                # refdoc=self.env.docname,
                refdomain="",
                refexplicit=True,
                refwarn=True,
            )
            innernode["classes"] = ["xref", "any"]
            if "tooltip" in self.options:
                ref_node["title"] = self.options["tooltip"]
        else:
            ref_node = nodes.reference()
            ref_node["refuri"] = uri
            if "tooltip" in self.options:
                ref_node["reftitle"] = self.options["tooltip"]

        self.set_source_info(ref_node)

        ref_node["classes"] = ["sphinx-bs", "btn", "text-wrap"] + self.options.get(
            "classes", ""
        ).split()
        ref_node += innernode
        # sphinx requires that a reference be inside a block element
        container = nodes.paragraph()
        container += ref_node

        return [container]
