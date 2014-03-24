"""URL configuration for the intranet django application container."""

from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from chemicals import urls as chemical_urls

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(chemical_urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
