# -*- encoding: utf-8 -*-

from django.core.mail import send_mail

def email_success_subscription(sender, instance, *args, **kwargs):
    send_mail(
        u'EventeX: Inscrição bem sucedida!',
        u'%s, parabéns! Você acaba de se inscrever no melhor evento do mundo. Aguarde nosso contato!' % instance.name,
        'eventex@eventex.com',
        [instance.email]
    )