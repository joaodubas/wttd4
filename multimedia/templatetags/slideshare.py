from django import template
from django.template import Node
from django.utils.translation import ugettext as _
from core.template import NodeContextMixin

register = template.Library()

def do_slideshare(parser, token):
    try:
        tagname, id_, doc = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, _(u'%r tag requer 2 argumentos.') % token.contents.split()[0]
    
    SlideshareNode(id_, doc)

class SlideshareNode(Node, NodeContextMixin):
    def __init__(self, id_, doc):
        self.id_ = id_
        self.doc = doc
    
    def render(self, context):
        actual_id = self.resolve_variable_context(self.id_, context)
        actual_doc = self.resolve_variable_context(self.doc, context)

        return self.render_context_to_template('multimedia/slideshare.html', {
            'id': actual_id,
            'doc': actual_doc,
        }, context)


register('slideshare', do_slideshare)