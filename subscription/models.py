# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.db import models
from subscription.signals import email_success_subscription

class Subscription(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('Nome'))
    email = models.EmailField(unique=True, verbose_name=_('E-mail'))
    cpf = models.CharField(max_length=11, unique=True, verbose_name=_('CPF'))
    phone = models.CharField(max_length=10, blank=True, verbose_name=_('Telefone'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado em'))

    class Meta:
        ordering = ('-created_at', )
        verbose_name = _(u'Inscrição')
        verbose_name_plural = _(u'Inscrições')
    
    def __unicode__(self):
        return _(u'%(name)s <%(email)s> inscrito em %(created_at)s') % self.__dict__
models.signals.post_save.connect(email_success_subscription, Subscription)

