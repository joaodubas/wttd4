from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request, template='index.html'):
    '''
    Returns the index page of the site
    '''
    return render_to_response(template, None, context_instance=RequestContext(request))