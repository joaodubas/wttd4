from django import template
from django.template import Node
from django.utils.translation import ugettext as _
from core.template import NodeContextMixin

register = template.Library()

def do_youtube(parser, token):
    try:
        tagname, id_ = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, _(u'%r tag requer 1 argumento.') % token.contents.split()[0]
    
    YoutubeNode(id_)

class YoutubeNode(Node, NodeContextMixin):
    def __init__(self, id_):
        self.id_ = id_
    
    def render(self, context):
        actual_id = self.resolve_variable_context(self.id_, context)

        return self.render_context_to_template('multimedia/youtube.html', {
            'id': actual_id
        }, context)


register('slideshare', do_youtube)