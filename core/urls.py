from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views',
    url(r'^palestrante/detalhe/(?P<pk>[\d]+)/(?P<slug>[\w\-]+)/$', 'detail_speaker', name='detail_speaker'),
    url(r'^palestrante/$', 'list_speaker', name='list_speaker'),
)

urlpatterns += patterns('core.views',
    url(r'^palestra/detalhe/(?P<pk>[\d]+)/(?P<slug>[\w\-]+)/$', 'detail_talk', name='detail_talk'),
    url(r'^palestra/$', 'list_talk', name='list_talk'),
    url(r'^slot/detalhe/$', 'detail_slot', name='detail_slot'),
    url(r'^slot/$', 'detail_slot', name='detail_slot'),
)