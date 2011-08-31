# -*- encoding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _
from django.forms.fields import EMPTY_VALUES

class PhoneWidget(forms.MultiWidget):
    """
    Creates a widget that contains two input type text
    """
    def __init__(self, attrs=None):
        widgets = (
            forms.TextInput(attrs=attrs),
            forms.TextInput(attrs=attrs)
        )
        super(PhoneWidget, self).__init__(widgets, attrs)
    
    def decompress(self, value):
        if not value:
            return [None, None]
        
        return value.split('-')


class PhoneField(forms.MultiValueField):
    """
    Field that receives two inputs, one related to the local area code
    and other that represents the phone number.
    """
    widget = PhoneWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(),
            forms.IntegerField()
        )
        super(PhoneField, self).__init__(fields, *args, **kwargs)
    
    def compress(self, data_list):
        if not data_list:
            return None
        if data_list[0] in EMPTY_VALUES:
            raise forms.ValidationError(_(u'DDD inválido'))
        if data_list[1] in EMPTY_VALUES:
            raise forms.ValidationError(_(u'Número inválido'))
        
        return '%s-%s' % tuple(data_list)

