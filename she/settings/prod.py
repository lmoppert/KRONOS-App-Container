from common import *
from secrets import DB_PASS

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

STATIC_ROOT = normpath(join(SITE_ROOT, "..", "static"))
STATIC_URL = 'https://lev-srv-590.eu.nli.net/'
MEDIA_ROOT = normpath(join(SITE_ROOT, "..", "static", "media"))
MEDIA_URL = 'https://lev-srv-590.eu.nli.net/media/'

ALLOWED_HOSTS = [
    '.eu.nli.net', '.eu.nli.net.',
    '.kronosww.com', '.kronosww.com.',
]

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
        'NAME': 'Substance_Portal',
        'USER': 'she',
        'PASSWORD': DB_PASS,
    }
}

MIDDLEWARE_CLASSES += (
    'django.contrib.auth.middleware.RemoteUserMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
)

SUIT_CONFIG['ADMIN_NAME'] = 'Chemicals PROD'
