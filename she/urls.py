"""URL configuration for the she django application container."""

from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from chemicals import urls as chemical_urls
from psa import urls as psa_urls

urlpatterns = i18n_patterns(
    '',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^styleguide$', TemplateView.as_view(template_name='styleguide.html')),
    url(r'^psa/', include(psa_urls)),
    url(r'', include(chemical_urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
