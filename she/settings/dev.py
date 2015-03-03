from common import *
from secrets import DB_PASS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS = ('debug_toolbar', ) + INSTALLED_APPS
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ('127.0.0.1', '10.49.20.25', '10.49.20.40')

SUIT_CONFIG['ADMIN_NAME'] = 'Chemicals DEV'
