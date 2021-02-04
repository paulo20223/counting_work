import os
from decimal import Decimal

import environ
from django.utils.translation import ugettext_lazy as _

from core.utils.base import get_settings_path

env = environ.Env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.dirname(os.path.abspath(__file__))
environ.Env.read_env(get_settings_path(CONFIG_DIR, ('production.env', 'sandbox.env', 'develop.env')))

VERSION = '0.0.1'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'core',
    'apps.company',
    'apps.invoice'
]

DEBUG = env.bool('DEBUG', default=True)
IS_SEND_EMAIL_NOTIFICATIONS = env('IS_SEND_EMAIL_NOTIFICATIONS', default=False)
if IS_SEND_EMAIL_NOTIFICATIONS:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'core.urls'
SECRET_KEY = env("SECRET_KEY")
CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': env.db("DATABASE_URL")
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'dist')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
ALLOWED_UPLOAD_IMAGES = ('png', 'bmp', 'jpeg')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

LOGIN_URL = '/api/v1/login'
LOGOUT_URL = '/api/v1/logout'

REDIS_HOST = env("REDIS_HOST", default="redis_db")
REDIS_PORT = env("REDIS_PORT", default="6379")

TWO_PLACES = Decimal(10) ** -2
