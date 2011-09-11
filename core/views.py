# -*- encoding: utf-8 -*-
from django.views.generic.simple import direct_to_template
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404
from django.http import Http404
from core.models import Speaker, Talk, Course

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

def list_talk(request, template="core/list_talk.html"):
    """
    List all talks that are registered on eventex
    """
    response = {
        'morning': Talk.objects.at_morning(),
        'afternoon': Talk.objects.at_afternoon(),
    }
    return direct_to_template(request, template, response)

def detail_talk(request, pk, template="core/detail_talk.html"):
    """
    Get the detail about a talk
    """
    response = {
        'talk': get_object_or_404(Talk, pk=pk)
    }
    return direct_to_template(request, template, response)

def list_course(request, template="core/list_course.html"):
    """
    List all courses that are registered on eventex
    """
    response = {
        'morning': Course.objects.at_morning(),
        'afternoon': Course.objects.at_afternoon(),
    }
    return direct_to_template(request, template, response)

def detail_course(request, pk, template="core/detail_course.html"):
    """
    Get the detail about a course
    """
    response = {
        'talk': get_object_or_404(Course, pk=pk)
    }
    return direct_to_template(request, template, response)
