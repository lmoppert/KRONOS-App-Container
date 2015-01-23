from common import *
from secrets import DB_PASS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATIC_ROOT = normpath(join(SITE_ROOT, "..", "static"))
STATIC_URL = 'https://lev-srv-577.eu.nli.net/'
MEDIA_ROOT = normpath(join(SITE_ROOT, "..", "static", "media"))
MEDIA_URL = 'https://lev-srv-577.eu.nli.net/media/'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'she',
        'USER': 'she',
        'PASSWORD': DB_PASS,
    },
    'legacy': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'she_Substance_Portal',
        'USER': 'she',
        'PASSWORD': DB_PASS,
    }
}

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
)

INSTALLED_APPS = ('debug_toolbar', 'django_extensions', ) + INSTALLED_APPS
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ('127.0.0.1', '10.49.20.25', '10.49.20.40')
