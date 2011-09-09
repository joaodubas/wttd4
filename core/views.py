# -*- encoding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.utils.translation import ugettext as _
from django.http import Http404
from core.models import Speaker

def list_speaker(request, template="core/list_speaker.html"):
    """
    List all speaker that are registered on eventex
    """
    speakers = Speaker.objects.all()
    response = { 'speakers': speakers, 'show_all_info': False }
    return direct_to_template(request, template, response)

def detail_speaker(request, pk, slug, template="core/detail_speaker.html"):
    """
    Get the details about one speaker
    """
    try:
        speaker = Speaker.objects.get(pk=pk, slug=slug)
    except Speaker.DoesNotExist:
        raise Http404(_(u'Houve algum problema tentando obter o palestrate! Você tem certeza de que ele existe?'))

    response = { 'speaker': speaker, 'show_all_info': True }
    return direct_to_template(request, template, response)

def list_talk(request):
    pass

def detail_talk(request):
    pass

def list_slot(request):
    pass

def detail_slot(request):
    pass
