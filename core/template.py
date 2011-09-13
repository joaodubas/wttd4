from django import template
from django.template import loader, Context

class NodeContextMixin(object):
    def resolve_variable_context(self, variable, context):
        try:
            value = variable.resolve(context)
        except template.VariableDoesNotExist:
            value = variable
        
        return value
    
    def render_context_to_template(self, template, additional_context, context):
        t = loader.get_template(template)
        c = Context(additional_context, autoescape=context.autoescape)
        return t.render(c)

