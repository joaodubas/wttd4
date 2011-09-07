# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext as _
from core.models import Speaker, Contact

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


admin.site.register(Speaker, SpeakerAdmin)


