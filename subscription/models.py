# -*- encoding: utf-8 -*-
from django.db import models

class Subscription(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nome')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    phone = models.CharField(max_length=10, blank=True, verbose_name='Telefone')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    class Meta:
        ordering = ('-created_at', )
        verbose_name = u'Inscrição'
        verbose_name_plural = u'Inscrições'
    
    def __unicode__(self):
        return '%(name)s inscrito em %(created_at)s' % (self, )
    
