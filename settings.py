"""
Django settings for arenafighter project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q6wz43x7$=6u2sc$92w-6i=2j-ptsixxp+v0juosf2r656ea(+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.join(PROJECT_ROOT, 'apps/'))


TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#TEMPLATE_DIRS = (
#    PROJECT_ROOT + '/arenafighter/templates/',
#)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
#            '/personal/templates',
            'apps',
            'apps/arenafighter',
            'apps/personal',
            'templates',
            # insert your TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]




# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'joshy',
    'grophy',
    'basesite',
    'arenafighter',
    'ckeditor',
#    'tinymce',
#    'south',
    'django_extensions',
)

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'arenafighter',
            'USER': 'arenafighter',
            'PASSWORD': 'arenafighter',
            'HOST': 'localhost',
            'PORT': '5432',
            'client_encoding': 'UTF8',
            'default_transaction_isolation': 'read committed',
            'timezone': 'UTC',
        }
    }
else:
    DATABASES = {}
    DATABASES['default'] = dj_database_url.config()

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
#        os.path.join(os.path.dirname(__file__), 'static'),
        )

STATIC_URL = '/static/'
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

#AUTH_PROFILE_MODULE = 'arenafighter.Profile'


# debug_toolbar settings
if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES += (
#        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    INSTALLED_APPS += (
#        'debug_toolbar',
    )

#    DEBUG_TOOLBAR_CONFIG = {
#        'INTERCEPT_REDIRECTS': False,
#    }
