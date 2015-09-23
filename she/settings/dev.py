from common import *
from secrets import PSQL_PASS, DB_PASS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

STATIC_ROOT = normpath(join(SITE_ROOT, "..", "static"))
STATIC_URL = 'https://static-dev.kronosww.com/'
MEDIA_ROOT = normpath(join(SITE_ROOT, "..", "static", "media"))
MEDIA_URL = 'https://static-dev.kronosww.com/media/'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'she',
        'USER': 'she',
        'PASSWORD': PSQL_PASS,
    },
    'legacy': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Substance_Portal',
        'USER': 'she',
        'PASSWORD': DB_PASS,
    },
    'legacy_psa': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DotNetNuke',
        'USER': 'she',
        'PASSWORD': DB_PASS,
    },
}

MIDDLEWARE_CLASSES += (
    'django.contrib.auth.middleware.RemoteUserMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
)

INSTALLED_APPS += ('debug_toolbar', )
INTERNAL_IPS = ('127.0.0.1', '10.49.20.25', '10.49.20.40')

SUIT_CONFIG['ADMIN_NAME'] = 'Chemicals STAGE'
