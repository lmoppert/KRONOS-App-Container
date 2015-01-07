"""Django settings for she project."""
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.conf import global_settings
from os.path import abspath, basename, dirname, join, normpath
from secrets import SECRET_KEY

BASE_DIR = dirname(dirname(abspath(__file__)))
SITE_NAME = basename(BASE_DIR)
SITE_ROOT = dirname(BASE_DIR)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['.eu.nli.net', '.kronosww.com']
ADMINS = (
    ('Lutz Moppert', 'lutz.moppert@kronosww.com'),
)
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

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = normpath(join(SITE_ROOT, "static"))
STATIC_URL = '/static/'

MEDIA_ROOT = normpath(join(SITE_ROOT, "media"))
MEDIA_URL = '/media/'

ROOT_URLCONF = '{}.urls'.format(SITE_NAME)
WSGI_APPLICATION = '{}.wsgi.application'.format(SITE_NAME)

INSTALLED_APPS = (
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'filer',
    'easy_thumbnails',
    'sekizai',
    'chemicals',
    'django_tables2',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'sekizai.context_processors.sekizai',
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

MIGRATION_MODULES = {
    'filer': 'filer.migrations_django',
}
