from common import *
from secrets import DB_PASS

DEBUG = False
TEMPLATE_DEBUG = DEBUG

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

STATIC_ROOT = normpath(join(SITE_ROOT, "..", "static"))
STATIC_URL = 'https://lev-srv-590.eu.nli.net/'
MEDIA_ROOT = normpath(join(SITE_ROOT, "..", "media"))
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
        'NAME': 'she_Substance_Portal',
        'USER': 'she',
        'PASSWORD': DB_PASS,
    }
}
