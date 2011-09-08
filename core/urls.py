from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views',
    url(r'palestrante/detalhe/(?P<pk>[\d]+)/(?P<slug>[\w\-]+)/$', 'detail_speaker', name='detail_speaker'),
    url(r'palestrante/$', 'list_speaker', name='list_speaker'),
)