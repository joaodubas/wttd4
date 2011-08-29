# -*- encoding: utf-8 -*-

from datetime import date
from django.contrib import admin
from django.conf.urls.defaults import patterns, url
from django.http import HttpResponse
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext
from subscription.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'today', 'paid', )
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at', )
    list_filter = ('created_at', 'paid', )
    actions = ['mark_as_paid']

    def today(self, obj):
        """
        Verifies if the subscription was created today
        """
        return date.today() == obj.created_at.date()
    today.boolean = True
    today.short_description = _(u'Inscrito hoje?')

    def mark_as_paid(self, request, queryset):
        """
        Mark a queryset of subscription as paid
        """
        count = queryset(paid=True)

        msg = ungettext(
            _(u'%(count)d inscrição foi marcada como paga!'),
            _(u'%(count)d inscrições foram marcadas como pagas!'),
            count
        ) % {'count': count}

        self.message_user(request, msg)
    mark_as_paid.short_description = _(u'Marcar inscrição como paga.')

    def export_csv(self, request):
        """
        Create a csv file and return it as a HttResponse
        """
        attrs = ['name', 'email', 'phone', 'paid']
        subscriptions = self.model.objects.all()

        def get_model_field(name):
            """
            Obtain the field of a model based on its name
            """
            return self.model._meta.get_field(name)

        rows = []
        for s in subscriptions:
            row = [getattr(s, attr) for attr in attrs]
            rows.append(','.join(['%s' % field for field in row]))
        rows.insert(0, ','.join([get_model_field(attr).verbose_name for attr in attrs]))

        response = HttpResponse('\r\n'.join(rows), mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=inscricoes.csv'

        return response
    
    def get_urls(self):
        """
        Override the get_urls method from ModelAdmin adding the export_subscriptions url
        """
        original_urls = super(SubscriptionAdmin, self).get_urls()
        new_urls = patterns('',
            url(r'export/$', self.admin_site.admin_view(self.export_csv), name='export_subscriptions')
        )

        return new_urls + original_urls


admin.site.register(Subscription, SubscriptionAdmin)
