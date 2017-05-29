"""Django settings for she project."""
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.messages import constants as messages
from os.path import abspath, basename, dirname, join, normpath
from secrets import SECRET_KEY, LDAP_USER_PW
import sys

BASE_DIR = dirname(dirname(abspath(__file__)))
SITE_NAME = basename(BASE_DIR)
SITE_ROOT = dirname(BASE_DIR)
sys.path.append(BASE_DIR)

DEBUG = False

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        normpath(join(SITE_ROOT, "templates")),
        normpath(join(SITE_ROOT, "psa", "templates")),
        normpath(join(SITE_ROOT, "chemicals", "templates")),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.debug',
            'django.template.context_processors.i18n',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.template.context_processors.tz',
            'django.contrib.messages.context_processors.messages',
            'django.template.context_processors.request',
        ],
    },
}, ]

ALLOWED_HOSTS = ['.eu.nli.net', '.kronosww.com']
ADMINS = [
    ('Lutz Moppert', 'lutz.moppert@kronosww.com'),
]
MANAGERS = ADMINS

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-de'
LANGUAGES = [
    ('en', _('English')),
    ('de', _('German')),
    ('nl', _('Dutch')),
    # ('nb', _('Norwegian Bokmal')),
]

SITE_ID = 1
SECRET_KEY = SECRET_KEY

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = normpath(join(SITE_ROOT, "static"))
STATICFILES_DIRS = [
    normpath(join(SITE_ROOT, "static")),
    normpath(join(SITE_ROOT, "chemicals", "static")),
]
STATIC_URL = '/static/'

MEDIA_ROOT = normpath(join(SITE_ROOT, "media"))
MEDIA_URL = '/media/'

ROOT_URLCONF = '{}.urls'.format(SITE_NAME)
WSGI_APPLICATION = '{}.wsgi.application'.format(SITE_NAME)

INSTALLED_APPS = [
    'suit',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdown_deux',
    'easy_thumbnails',
    'filer',
    'mptt',
    'chemicals',
    'psa',
    'django_tables2',
    'django_extensions',
    'ldap_sync',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

THUMBNAIL_PROCESSORS = [
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
]

# MIGRATION_MODULES = {
#     'filer': 'filer.migrations_django',
# }

# Settings for LDAP synchronisation
LDAP_SYNC_URI = "ldap://kro-lev-srv-600.kronosww.com:389"
LDAP_SYNC_BASE = "OU=EU,DC=Kronosww,DC=com"
LDAP_SYNC_BASE_USER = "CN=AD Query,OU=Service Accounts,OU=LEV,OU=DE," \
    "OU=EU,DC=Kronosww,DC=com"
LDAP_SYNC_BASE_PASS = LDAP_USER_PW
LDAP_SYNC_USER_FILTER = "(&(objectCategory=person)(objectClass=User)" \
    "(memberOf=CN=LEV-GG-Chemicals,OU=Global,OU=Groups,OU=LEV,OU=DE," \
    "OU=EU,DC=Kronosww,DC=com))"
LDAP_SYNC_USER_ATTRIBUTES = {
    "userPrincipalName": "username",
    "givenName": "first_name",
    "sn": "last_name",
    "mail": "email",
}
LDAP_SYNC_GROUP_FILTER = "(&(objectclass=group)" \
    "(memberOf=CN=LEV-GG-Chemicals,OU=Global,OU=Groups,OU=LEV,OU=DE," \
    "OU=EU,DC=Kronosww,DC=com))"
LDAP_SYNC_GROUP_ATTRIBUTES = {"cn": "name", }

SUIT_CONFIG = {
    'SEARCH_URL': '',
    'MENU_ICONS': {
        'auth': 'icon-user',
        'chemicals': 'icon-tint',
        'filer': 'icon-folder-open',
        'psa': 'icon-headphones',
    },
}
CRISPY_TEMPLATE_PACK = 'bootstrap3'

MESSAGE_TAGS = {messages.ERROR: 'danger'}

FILEBROWSER_LIST_PER_PAGE = 10000
