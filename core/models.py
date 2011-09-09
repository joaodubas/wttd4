# -*- encoding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _
from core.signals import slugify_name
import hashlib
import urllib
import datetime

class Speaker(models.Model):
    name = models.CharField(max_length=256, verbose_name=_(u'Nome'))
    slug = models.SlugField(unique=True, verbose_name=_(u'Slug do nome'))
    url = models.URLField(verify_exists=False, verbose_name=_(u'Site'))
    description = models.TextField(blank=True, verbose_name=_(u'Descrição'))
    avatar = models.FileField(upload_to='palestrante', blank=True, null=True, verbose_name=_(u'Avatar'))

    class Meta:
        ordering = ('name', )
        verbose_name = _(u'palestrante')
        verbose_name_plural = _(u'palestrantes')

    def __unicode__(self):
        return self.name
    
    @models.permalink
    def get_absolute_url(self):
        return ('detail_speaker', (), {'pk': self.pk, 'slug': self.slug})
    
    @property
    def get_avatar(self):
        default = '%s%s' % (settings.STATIC_URL, 'images/icon/avatar.jpg', )
        if self.avatar:
            return self.avatar
        elif self.contact_set.filter(kind='E').count():
            email = self.contact_set.all()[:1][0]
            url = 'http://www.gravatar.com/avatar/%(email_hash)s?%(qs)s'
            url = url % {'email_hash': hashlib.md5(email.value).hexdigest(), 'qs': urllib.urlencode({'d': default, 's': '80'})}
            return url
        else:
            return default
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


class PeriodManager(models.Manager):
    midday = datetime.time(12)

    def at_morning(self):
        qs = self.filter(start_time__lt=self.midday)
        qs = qs.order_by('start_time')
        return qs
    
    def at_afternoon(self):
        qs = self.filter(start_time__gte=self.midday)
        qs = qs.order_by('start_time')
        return qs


class Talk(models.Model):
    title = models.CharField(max_length=256, verbose_name=_(u'título'))
    description = models.TextField(verbose_name=_(u'descrição'))
    start_time = models.TimeField(blank=True, verbose_name=_(u'hora de início'))
    speakers = models.ManyToManyField('Speaker', verbose_name=_(u'palestrantes'))

    objects = PeriodManager()

    class Meta:
        ordering = ('start_time', 'title', )
        verbose_name = _(u'palestra')
        verbose_name_plural = _(u'palestras')
    
    def __unicode__(self):
        return self.title


class Course(Talk):
    slots = models.IntegerField()
    notes = models.TextField()

    objects = PeriodManager()


class Media(models.Model):
    MEDIAS = (
        ('SL', 'SlideShare'),
        ('YT', 'Youtube'),
    )

    talk = models.ForeignKey('Talk')
    type = models.CharField(max_length=2, choices=MEDIAS)
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return '%s <%s>' % (self.title, self.talk.title, )

