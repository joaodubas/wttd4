from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views',
    url(r'^palestrante/detalhe/(?P<pk>[\d]+)/(?P<slug>[\w\-]+)/$', 'detail_speaker', name='detail_speaker'),
    url(r'^palestrante/$', 'list_speaker', name='list_speaker'),
)

urlpatterns += patterns('core.views',
    url(r'^palestra/detalhe/(?P<pk>[\d]+)/$', 'detail_talk', name='detail_talk'),
    url(r'^palestra/$', 'list_talk', name='list_talk'),
    url(r'^curso/detalhe/(?P<pk>[\d]+)/$', 'detail_course', name='detail_course'),
    url(r'^curso/$', 'list_course', name='list_course'),
)