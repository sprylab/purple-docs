# -*- coding: utf-8 -*-
"""
Custom directive for purple properties
"""

import sphinx
from docutils import nodes
from docutils.parsers.rst import directives

from toggle_box import ToggleBox, toggle_box_node


class versioned_toggle_box_node(toggle_box_node, nodes.Element):
    pass


class VersionedToggleBox(ToggleBox):
    """
    A versioned toggle box entry, displayed (if configured) in the form of an admonition.
    """

    node_class = versioned_toggle_box_node
    has_content = True
    required_arguments = 0
    optional_arguments = 8
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
        'color': directives.class_option,
        'only-available-for': directives.unchanged,
        'not-available-for': directives.unchanged,
        'versionadded-android': directives.unchanged,
        'versionadded-ios': directives.unchanged,
        'versionadded-web-kiosk': directives.unchanged,
        'versionadded-web-player': directives.unchanged,
        'versionadded-composer': directives.unchanged,
        'versionchanged': directives.unchanged,
        'type': directives.unchanged,
        'values': directives.unchanged,
        'default': directives.unchanged,
        'story': directives.unchanged
    }

    # todo versionchanged
    def header_text(self):
        text = []
        if self.options.get('only-available-for') \
                or self.options.get('not-available-for') \
                or self.options.get('versionadded-android') \
                or self.options.get('versionadded-ios') \
                or self.options.get('versionadded-web-kiosk') \
                or self.options.get('versionadded-web-player') \
                or self.options.get('versionadded-composer') \
                or self.options.get('versionchanged') \
                or self.options.get('type') \
                or self.options.get('values') \
                or self.options.get('default'):
            # text += ".. container:: custom-text\n"
            # text += "\n"
            if self.options.get('only-available-for'):
                value = self.options["only-available-for"]
                container = nodes.container()
                container.attributes["classes"] = [u"versionadded"]
                p = nodes.paragraph()
                p += nodes.strong(text=u"This is only available for " + value)
                container += p
                text.append(container)
            if self.options.get('not-available-for'):
                value = self.options["not-available-for"]
                container = nodes.container()
                container.attributes["classes"] = [u"versionadded"]
                p = nodes.paragraph()
                p += nodes.strong(text=u"This is not available for " + value)
                container += p
                text.append(container)
            if self.options.get('versionadded-android'):
                value = self.options["versionadded-android"]
                container = nodes.container()
                container.attributes["classes"] = [u"versionadded"]
                p = nodes.paragraph()
                p += nodes.strong(text=u"New in version (Android): ")
                p += nodes.Text(value)
                container += p
                text.append(container)
            if self.options.get('versionadded-ios'):
                value = self.options["versionadded-ios"]
                container = nodes.container()
                container.attributes["classes"] = [u"versionadded"]
                p = nodes.paragraph()
                p += nodes.strong(text=u"New in version (iOS): ")
                p += nodes.Text(value)
                container += p
                text.append(container)
            if self.options.get('versionadded-web-kiosk'):
                value = self.options["versionadded-web-kiosk"]
                container = nodes.container()
                container.attributes["classes"] = [u"versionadded"]
                p = nodes.paragraph()
                p += nodes.strong(text=u"New in version (Web Kiosk): ")
                p += nodes.Text(value)
                container += p
                text.append(container)
            if self.options.get('versionadded-web-player'):
                value = self.options["versionadded-web-player"]
                container = nodes.container()
                container.attributes["classes"] = [u"versionadded"]
                p = nodes.paragraph()
                p += nodes.strong(text=u"New in version (Web Player): ")
                p += nodes.Text(value)
                container += p
                text.append(container)
            if self.options.get('versionadded-composer'):
                value = self.options["versionadded-composer"]
                container = nodes.container()
                container.attributes["classes"] = [u"versionadded"]
                p = nodes.paragraph()
                p += nodes.strong(text=u"New in version (Composer): ")
                p += nodes.Text(value)
                container += p
                text.append(container)
            if self.options.get('versionchanged'):
                value = self.options["versionchanged"]
                container = nodes.container()
                container.attributes["classes"] = [u"versionchanged"]
                p = nodes.paragraph()
                p += nodes.strong(text=u"Changed in version: ")
                p += nodes.Text(value)
                container += p
                text.append(container)
            if self.options.get('type'):
                value = self.options["type"]
                container = nodes.container()
                container.attributes["classes"] = [u"custom-text-newline"]
                p = nodes.paragraph()
                p += nodes.strong(text="Type: ")
                code = nodes.literal(text=value)
                code.attributes["classes"] = [u"code"]
                p += code
                container += p
                text.append(container)
            if self.options.get('values'):
                container = nodes.container()
                container.attributes["classes"] = [u"custom-text-newline"]
                p = nodes.paragraph()
                p += nodes.strong(text=u"Values: ")
                values = escape_split(self.options["values"], ',')
                for value in values:
                    code = nodes.literal(text=value.strip())
                    code.attributes["classes"] = [u"code"]
                    p += code
                    p += nodes.Text(" ")
                container += p
                text.append(container)
            if self.options.get('default'):
                value = self.options["default"]
                container = nodes.container()
                container.attributes["classes"] = [u"custom-text-newline"]
                p = nodes.paragraph()
                p += nodes.strong(text=u"Default: ")
                code = nodes.literal(text=value)
                code.attributes["classes"] = [u"code"]
                p += code
                container += p
                text.append(container)
        if text:
            text.append(nodes.line_block(children=nodes.line()))
        return text

    def footer_text(self):
        text = ""
        # gap = "\n" + "|\n" + "\n"
        # if self.options.get('story'):
        #     text += gap
        #     text += ".. container::\n"
        #     text += "\n"
        #     text += "   **Redmine Story:** :purple_issue:`" + self.options[
        #         'story'] + "`\n"
        return text


def visit_purple_versioned_toggle_box_node(self, node):
    self.visit_admonition(node)


def depart_purple_versioned_toggle_box_node(self, node):
    self.depart_admonition(node)


def setup(app):
    app.add_node(versioned_toggle_box_node,
                 html=(visit_purple_versioned_toggle_box_node,
                       depart_purple_versioned_toggle_box_node),
                 latex=(visit_purple_versioned_toggle_box_node,
                        depart_purple_versioned_toggle_box_node),
                 text=(visit_purple_versioned_toggle_box_node,
                       depart_purple_versioned_toggle_box_node),
                 man=(visit_purple_versioned_toggle_box_node,
                      depart_purple_versioned_toggle_box_node),
                 texinfo=(visit_purple_versioned_toggle_box_node,
                          depart_purple_versioned_toggle_box_node))

    app.add_directive('versioned-toggle-box', VersionedToggleBox)
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
