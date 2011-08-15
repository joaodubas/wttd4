from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'core.views.homepage', name='home'),
)

# urlpatterns += patterns('',
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#     url(r'^admin/', include(admin.site.urls)),
# )

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()