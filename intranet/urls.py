"""URL configuration for intranet project."""

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from chemicals import urls as chemical_urls
from django.conf import settings

admin.autodiscover()

urlpatterns = i18n_patterns(
    '',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chemicals/', include(chemical_urls)),
)

if settings.DEBUG:
    from debug_toolbar import urls as dt_urls

    urlpatterns = i18n_patterns(
        '',
        url(r'^__debug__/', include(dt_urls)),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
