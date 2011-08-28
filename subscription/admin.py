from datetime import date
from django.contrib import admin
from django.utils.translation import ugettext as _
from subscription.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'today', )
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at', )
    list_filter = ('created_at', )
    actions = ['mark_as_paid']

    def today(self, obj):
        return date.today() == obj.created_at.date()
    today.boolean = True
    today.short_description = _(u'Inscrito hoje?')


admin.site.register(Subscription, SubscriptionAdmin)