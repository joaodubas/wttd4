from datetime import date
from django.contrib import admin
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


admin.site.register(Subscription, SubscriptionAdmin)