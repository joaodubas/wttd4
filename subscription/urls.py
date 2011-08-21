from django.conf.urls.defaults import patterns, url
from vendor.route import route

urlpatterns = patterns('subscription.views',
    route(r'^nova/$', GET='new', POST='create', name='subscribe'),
    url(r'^sucesso/(?P<id>\d+)/$', 'success', name='success'),
)