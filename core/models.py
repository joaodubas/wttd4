# -*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from core.signals import slugify_name

# import datetime

class Speaker(models.Model):
    name = models.CharField(max_length=256, verbose_name=_(u'Nome'))
    slug = models.SlugField(unique=True, verbose_name=_(u'Slug do nome'))
    url = models.URLField(verify_exists=False, verbose_name=_(u'Site'))
    description = models.TextField(blank=True, verbose_name=_(u'Descrição'))
    avatar = models.FileField(upload_to='palestrante', blank=True, null=True, verbose_name=_(u'Avatar'))
    # desafio: colocar email e buscar o gravatar do palestrante

    class Meta:
        ordering = ('name', )
        verbose_name = _(u'palestrante')
        verbose_name_plural = _(u'palestrantes')

    def __unicode__(self):
        return self.name
models.signals.pre_save.connect(slugify_name, Speaker)


class KindContactManager(models.Manager):
    def __init__(self, kind, *args, **kwargs):
        super(KindContactManager, self).__init__(*args, **kwargs)
        self.kind = kind
    
    def get_query_set(self):
        qs = super(KindContactManager, self).get_query_set()
        qs = qs.filter(kind=self.kind)
        return qs


class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('E-mail')),
        ('F', _('Fax')),
    )

    speaker = models.ForeignKey('Speaker', verbose_name=_(u'Palestrante'))
    kind = models.CharField(max_length=1, choices=KINDS)
    value = models.CharField(max_length=256)

    objects = models.Manager()
    phones = KindContactManager('P')
    emails = KindContactManager('E')
    faxes = KindContactManager('F')

    class Meta:
        ordering = ('speaker__name', 'kind', )
        verbose_name = _(u'contato')
        verbose_name_plural = _(u'contatos')

    def __unicode__(self):
        return '%(speaker)s <%(kind)s: %(value)s>' % {'speaker': self.speaker.name,
                                                        'kind': self.get_kind_display(),
                                                        'value': self.value}


# class PeriodManager(models.Manager):
#     midday = datetime.time(12)

#     def at_morning(self):
#         qs = self.filter(start_time__lt=self.midday)
#         qs = qs.order_by('start_time')
#         return qs
    
#     def at_afternoon(self):
#         qs = self.filter(start_time__gte=self.midday)
#         qs = qs.order_by('start_time')
#         return qs


# class Talk(models.Model):
#     title = models.CharField(max_length=256, verbose_name=_(u'título'))
#     description = models.TextField(verbose_name=_(u'descrição'))
#     start_time = models.TimeField(blank=True, verbose_name=_(u'hora de início'))
#     speakers = models.ManyToManyField('Speaker', verbose_name=_(u'palestrantes'))

#     objects = PeriodManager()

#     class Meta:
#         ordering = ('start_time', 'title', )
#         verbose_name = _(u'palestra')
#         verbose_name_plural = _(u'palestras')
    
#     def __unicode__(self):
#         return self.title


# class Course(Talk):
#     slots = models.IntegerField()
#     notes = models.TextField()

#     objects = PeriodManager()


# class Media(models.Model):
#     MEDIAS = (
#         ('SL', 'SlideShare'),
#         ('YT', 'Youtube'),
#     )

#     talk = models.ForeignKey('Talk')
#     type = models.CharField(max_length=2, choices=MEDIAS)
#     title = models.CharField(max_length=256)
#     description = models.TextField(blank=True)

#     def __unicode__(self):
#         return '%s <%s>' % (self.title, self.talk.title, )

