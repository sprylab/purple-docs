# -*- coding: utf-8 -*-
"""
Custom directive for a toggle box
"""

import sphinx
from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from docutils.parsers.rst.roles import set_classes
from docutils.statemachine import ViewList, StringList


class toggle_box_node(nodes.Admonition, nodes.Element):
    pass


class ToggleBox(BaseAdmonition):
    """
    Content displayed (if configured) in the form of an admonition.
    """

    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
        'color': directives.class_option
    }
    has_content = True

    node_class = toggle_box_node
    required_arguments = 0
    optional_arguments = 8

    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['toggle-box-node', 'hint', 'toggle']
        else:
            self.options['class'] += ['toggle-box-node', 'hint', 'toggle']

        # Set color if available
        if self.options.get('color'):
            self.options['class'] += self.options.get('color')

        set_classes(self.options)
        self.assert_has_content()

        # Create content text
        text = "\n".join(self.content) + "\n"
        # Footer
        text += self.footer_text()

        tb_node = self.node_class(text, **self.options)
        self.add_name(tb_node)
        # if self.options.get('color'):
        #     tb_node.attributes["color"] = self.options.get('color')

        # Add title container
        title_text = " ".join(self.arguments)
        textnodes, messages = self.state.inline_text(title_text,
                                                     self.lineno)
        title = nodes.title(title_text, '', *textnodes)
        title.source, title.line = (
            self.state_machine.get_source_and_line(self.lineno))
        classes = ['toggle-box-title', 'header']
        title.attributes['class'] = classes
        title.attributes['classes'] = classes
        tb_node += title
        tb_node += messages
        tb_node += self.header_text()

        # Parse the text into the content_container
        # https://groups.google.com/forum/?fromgroups#!searchin/sphinx-dev/directive%7Csort:relevance/sphinx-dev/l4fHrIJfwq4/Qk_Rz_OsBgAJ
        self.state.nested_parse(
            StringList(ViewList(text.splitlines(), parent=self.content.parent)),
            self.content_offset, tb_node
        )

        return [tb_node]

    def header_text(self):
        return []

    def footer_text(self):
        return ''


def visit_toggle_box_node(self, node):
    self.visit_admonition(node)


def depart_toggle_box_node(self, node):
    self.depart_admonition(node)


def setup(app):
    app.add_node(toggle_box_node,
                 html=(visit_toggle_box_node, depart_toggle_box_node),
                 latex=(visit_toggle_box_node, depart_toggle_box_node),
                 text=(visit_toggle_box_node, depart_toggle_box_node),
                 man=(visit_toggle_box_node, depart_toggle_box_node),
                 texinfo=(visit_toggle_box_node, depart_toggle_box_node))

    app.add_directive('toggle-box', ToggleBox)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}


# from: http://stackoverflow.com/questions/18092354/python-split-string-without-splitting-escaped-character/29107566#29107566
def escape_split(s, delim):
    i, res, buf = 0, [], ''
    while True:
        j, e = s.find(delim, i), 0
        if j < 0:  # end reached
            return res + [buf + s[i:]]  # add remainder
        while j - e and s[j - e - 1] == '\\':
            e += 1  # number of escapes
        d = e // 2  # number of double escapes
        if e != d * 2:  # odd number of escapes
            buf += s[i:j - d - 1] + s[j]  # add the escaped char
            i = j + 1  # and skip it
            continue  # add more to buf
        res.append(buf + s[i:j - d])
        i, buf = j + len(delim), ''  # start after delim
