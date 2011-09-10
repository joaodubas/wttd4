# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _

class Media(models.Model):
    MEDIAS = (
        ('SL', 'SlideShare'),
        ('YT', 'Youtube'),
    )

    talk = models.ForeignKey('core.Talk', verbose_name=_(u'palestra'))
    type = models.CharField(max_length=2, choices=MEDIAS, verbose_name=_(u'tipo de mídia'))
    title = models.CharField(max_length=256, verbose_name=_(u'título'))
    media_id = models.CharField(max_length=256, verbose_name=_(u'id da mídia'))

    def __unicode__(self):
        return '%s <%s>' % (self.title, self.talk.title, )

