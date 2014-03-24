"""Django settings for intranet project."""
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.conf import global_settings
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '!hnmwz_vidp!uxa4rkiyi$9x4y4&swvfw1sko2kvu074+(nx$&'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['.eu.nli.net']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_extensions',
    'debug_toolbar',
    'filer',
    'easy_thumbnails',
    'modeltranslation',
    'south',
    'sekizai',
    'chemicals',
    'django_tables2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai',
)

ROOT_URLCONF = 'intranet.urls'
WSGI_APPLICATION = 'intranet.wsgi.application'

LANGUAGE_CODE = 'de-de'
LANGUAGES = [
    ('en', _('English')),
    ('de', _('German')),
    ('nl', _('Dutch')),
    ('nb', _('Norwegian Bokmal')),
]
TIME_ZONE = 'Europe/Berlin'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = '/var/www/intranet/static/'
STATIC_URL = '/static/'

DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ('127.0.0.1', '10.49.20.25', '10.49.20.40')

try:
    from local_settings import *
except:
    pass
