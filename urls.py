from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', kwargs={'template': 'index.html'}, name='home'),
)

admin.autodiscover()
urlpatterns += patterns('',
    url(r'^', include('core.urls')),
    url(r'^inscricao/', include('subscription.urls', namespace='subscription')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()