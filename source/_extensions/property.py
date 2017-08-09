# -*- coding: utf-8 -*-
"""
Custom directive for purple properties
"""

import sphinx
from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.environment import NoUri
from sphinx.locale import _

from versioned_toggle_box import versioned_toggle_box_node
from versioned_toggle_box import VersionedToggleBox


# An property node and property-list directive which lists all property nodes
# based on property and sphinx.ext.todo
class purple_property_node(versioned_toggle_box_node, nodes.Element):
    pass


class PropertyListNode(nodes.General, nodes.Element):
    pass


class Property(VersionedToggleBox):
    node_class = purple_property_node

    def run(self):
        # add property class so that we can find it later
        if not self.options.get('class'):
            self.options['class'] = ['property']
        else:
            self.options['class'] += ['property']
        (node,) = VersionedToggleBox.run(self)

        env = self.state.document.settings.env
        targetid = 'index-%s' % env.new_serialno('index')
        targetnode = nodes.target('', '', ids=[targetid])
        return [targetnode, node]


def process_properties(app, doctree):
    # collect all app-properties in the environment
    # this is not done in the directive itself because some transformations
    # must have already been run, e.g. substitutions
    env = app.builder.env
    if not hasattr(env, 'all_properties_list'):
        env.all_properties_list = []
    for node in doctree.traverse(purple_property_node):
        # ignore all entries in about.rst
        if env.docname != 'about':
            try:
                targetnode = node.parent[node.parent.index(node) - 1]
                if not isinstance(targetnode, nodes.target):
                    raise IndexError
            except IndexError:
                targetnode = None
            newnode = node.deepcopy()
            del newnode['ids']
            env.all_properties_list.append({
                'docname': env.docname,
                'source': node.source or env.doc2path(env.docname),
                'property': newnode,
                'target': targetnode,
                'name': newnode.children[0].children[0]
            })


class PropertyList(Directive):
    """
    A list of all property entries.
    """

    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        # Simply insert an empty property_list node which will be replaced later
        # when process_property_nodes is called
        return [PropertyListNode('')]


def process_property_nodes(app, doctree, fromdocname):
    # Replace all property nodes with a list of the collected properties.
    # Augment each property with a backlink to the original location.
    env = app.builder.env

    for node in doctree.traverse(PropertyListNode):

        # sort by name
        sorted_list = sorted(env.all_properties_list, key=lambda n: n['name'])
        content = []

        for property_node in sorted_list:
            property_entry = property_node['property']
            env.resolve_references(property_entry, property_node['docname'],
                                   app.builder)
            # Insert into the property-list
            para = nodes.paragraph(classes=['property-source'])

            description = _('(<<original page>>)')
            desc1 = description[:description.find('<<')]
            desc2 = description[description.find('>>') + 2:]
            para += nodes.Text(desc1, desc1)

            newnode = nodes.reference('', '', internal=True)
            innernode = nodes.emphasis(_('original page'), _('original page'))
            try:
                newnode['refuri'] = app.builder.get_relative_uri(
                    fromdocname, property_node['docname'])
                newnode['refuri'] += '#' + property_node['target']['refid']
            except NoUri:
                # ignore if no URI can be determined, e.g. for LaTeX output
                pass
            newnode.append(innernode)
            para += newnode
            para += nodes.Text(desc2, desc2)

            property_entry[1].append(para)
            content.append(property_entry)

        # Add content container
        content_container = nodes.container('')
        content_container.attributes['classes'] += ['custom-toggle-list']
        content_container.insert(1, content)
        node.replace_self(content_container)


def purge_properties(app, env, docname):
    if not hasattr(env, 'all_properties_list'):
        return
    env.all_properties_list = [property for property in env.all_properties_list
                               if property['docname'] != docname]


def merge_info(app, env, docnames, other):
    if not hasattr(other, 'all_properties_list'):
        return
    if not hasattr(env, 'all_properties_list'):
        env.all_properties_list = []
    env.all_properties_list.extend(other.all_properties_list)


def visit_purple_property_node(self, node):
    self.visit_admonition(node)


def depart_purple_property_node(self, node):
    self.depart_admonition(node)


def setup(app):
    app.add_node(PropertyListNode)
    app.add_node(purple_property_node,
                 html=(visit_purple_property_node, depart_purple_property_node),
                 latex=(
                     visit_purple_property_node, depart_purple_property_node),
                 text=(visit_purple_property_node, depart_purple_property_node),
                 man=(visit_purple_property_node, depart_purple_property_node),
                 texinfo=(
                     visit_purple_property_node, depart_purple_property_node))

    app.add_directive('property', Property)
    app.add_directive('property-list', PropertyList)
    app.connect('doctree-read', process_properties)
    app.connect('doctree-resolved', process_property_nodes)
    app.connect('env-purge-doc', purge_properties)
    app.connect('env-merge-info', merge_info)

    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
