from common import *
from secrets import PSQL_PASS

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

STATIC_ROOT = normpath(join(SITE_ROOT, "..", "static"))
STATIC_URL = 'https://chemicals.kronosww.com:8443/'
MEDIA_ROOT = normpath(join(SITE_ROOT, "..", "static", "media"))
MEDIA_URL = 'https://chemicals.kronosww.com:8443/media/'

ALLOWED_HOSTS = [
    '.kronosww.com', '.kronosww.com.',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'levp1.kronosww.com'
SERVER_EMAIL = 'chemicals@kronosww.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'she',
        'USER': 'she',
        'PASSWORD': PSQL_PASS,
    },
}

MIDDLEWARE_CLASSES += (
    'django.contrib.auth.middleware.RemoteUserMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
)

SUIT_CONFIG['ADMIN_NAME'] = 'Chemicals PROD'
