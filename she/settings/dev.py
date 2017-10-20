"""Django settings for she development server."""
# -*- coding: utf-8 -*-
from common import *
from secrets import PSQL_PASS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATIC_ROOT = normpath(join(SITE_ROOT, "..", "static", "dev-she"))
STATIC_URL = 'https://chemicals-dev.kronosww.com:8443/dev-she/'
MEDIA_ROOT = normpath(join(SITE_ROOT, "..", "static", "media"))
MEDIA_URL = 'https://chemicals-dev.kronosww.com:8443/media/'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'dev_she',
        'USER': 'she',
        'PASSWORD': PSQL_PASS,
    },
}

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
)

INSTALLED_APPS += ('debug_toolbar', )
INTERNAL_IPS = ('127.0.0.1', '10.49.20.50', '10.49.20.40')

SUIT_CONFIG['ADMIN_NAME'] = 'Chemicals DEV'
