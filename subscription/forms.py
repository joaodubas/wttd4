# -*- encoding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _
from subscription.models import Subscription
from core.fields import PhoneField, PhoneWidget

class SubscriptionForm(forms.ModelForm):
    phone = PhoneField(required=False, label=_(u'Telefone'), widget=PhoneWidget(attrs = {'class': 'phone'}))
    class Meta:
        model = Subscription
        exclude = ('created_at', 'paid', )

