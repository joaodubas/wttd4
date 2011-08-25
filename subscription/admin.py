from datetime import date
from django.contrib import admin
from subscription.models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'today', )
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'email', 'phone', 'created_at', )
    list_filter = ('created_at', )

    def today(self, obj):
        return date.today() == obj.created_at.date()
    today.boolean = True
    today.short_description = u'Inscrito hoje?'


admin.site.register(Subscription, SubscriptionAdmin)