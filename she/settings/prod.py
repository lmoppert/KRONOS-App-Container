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
