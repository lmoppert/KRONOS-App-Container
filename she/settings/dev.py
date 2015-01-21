from common import *
from secrets import DB_PASS

# #Active Directory Authentication
# AD_DNS_NAME = 'eu.nli.net'
# AD_LDAP_PORT = 389
# AD_LDAP_URL = 'ladp://%s:%s' % (AD_DNS_NAME, AD_LDAP_PORT)
# AD_SEARCH_DN = 'dc=eu,dc=nli,dc=net'
# AD_NT4_DOMAIN = 'NLI'
# AD_SEARCH_FIELDS = ['mail', 'givenName', 'sn', 'sAMAccountName', 'memberOf']
# AD_MEMBERSHIP_ADMIN = ['LEV-GG-Intranet-Admins']
# AD_MEMBERSHIP_REQ = ['LEV-GG-Intranet']
#
# AD_DEBUG = True
# AD_DEBUG_FILE = 'logs/ldap.debug'

# AUTHENTICATION_BACKENDS = (
#     '.backend.ActiveDirectoryAuthenticationBackend',
# )
#

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
        'NAME': 'she_Substance_Portal',
        'USER': 'she',
        'PASSWORD': DB_PASS,
    }
}

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
INSTALLED_APPS = ('debug_toolbar', 'django_extensions', ) + INSTALLED_APPS
DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ('127.0.0.1', '10.49.20.25', '10.49.20.40')
