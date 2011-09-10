# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from core.models import Speaker, Contact, Talk, Course
from multimedia.admin import MediaTabularInline

class ContactTabularInline(admin.TabularInline):
    model = Contact
    extras = 1


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'telephone', 'email', 'fax', )
    search_fields = ('name', 'contact_set__value', )
    prepopulated_fields = {'slug': ('name', )}
    inlines = (ContactTabularInline, )

    def _contact(self, obj, kind):
        try:
            return obj.contact_set.filter(kind=kind)[:1][0].value
        except (Contact.DoesNotExist, IndexError):
            return '-'

    def telephone(self, obj):
        return self._contact(obj, 'P')
    telephone.short_description = _(u'Telefone')
    
    def email(self, obj):
        return self._contact(obj, 'E')
    email.short_description = _(u'E-mail')
    
    def fax(self, obj):
        return self._contact(obj, 'F')
    fax.short_description = _(u'Fax')


class TalkAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'list_speakers', )
    inlines = (MediaTabularInline, )

    def list_speakers(self, obj):
        if not obj.speakers.all().count():
            return '<strong>&emdash;</strong>'

        to_speaker = '<a href="%s">%s</a>'
        speakers = [to_speaker % (reverse('admin:core_speaker_change', args=[speaker.pk]), speaker.name) for speaker in obj.speakers.all()]
        return ', '.join(speakers)
    list_speakers.short_description = _(u'Palestrantes')
    list_speakers.allow_tags = True


class CourseAdmin(TalkAdmin):
    list_display = TalkAdmin.list_display + ('slots', )


admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
admin.site.register(Course, CourseAdmin)
