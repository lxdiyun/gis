"""
Django settings for gis project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y=$#&5kv^e$pj_f=m6-uuzoh9$du7snqx9(hd@e6o88+r((stj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'dajaxice',
    'dajax',
    'imagekit',
    'haystack',
    'utils',
    'inscription',
    'debug_toolbar',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    'django.core.context_processors.request',
    "django.contrib.messages.context_processors.messages")

ROOT_URLCONF = 'gis.urls'

WSGI_APPLICATION = 'gis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Hong_Kong'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/website/static/'
STATIC_ROOT = '/home/www/gis/static/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'dajaxice.finders.DajaxiceFinder',
)


MEDIA_URL = '/website/media/'
MEDIA_ROOT = '/home/www/gis/media/'

GOOGLE_MAPS_API_KEY = 'AIzaSyC0EnKraozzSAB8B5fqSN3w-vFWChYdWIQ'
GOOGLE_MAPS_API_URL = 'http://ditu.google.com/maps/api/js'

# DEBUG_TOOLBAR_CONFIG
if DEBUG is True:
    INTERNAL_IPS = ('127.00.0.1', '10.0.2.2')

    def custom_show_toolbar(request):
        return True  # Always show toolbar, for example purposes only.

    DEBUG_TOOLBAR_CONFIG = {
#        'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
        'TAG': 'body',
    }

# logging
if DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['console'],
                'level': 'ERROR',
                'propagate': False,
            },
            'dajaxice': {
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': True,
            }
        }
    }

# haystack
HAYSTACK_CONNECTIONS = {
    # whoosh
    'default': {
                'ENGINE': 'utils.haystack.backends.zh_yaha_whoosh_backend.WhooshEngine',
                'PATH': os.path.join(os.path.dirname(__file__), '../whoosh_index'),
            },
    # elasticsearch
#    'default': {
#        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#        'URL': 'http://127.0.0.1:9200/',
#        'INDEX_NAME': 'haystack',
#    },
}
#HAYSTACK_CUSTOM_HIGHLIGHTER = "utils.haystack.highlighting.CompleteHighlighter"
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# dajaxice js file endpoint fix
if len(sys.argv) > 1:
    if 'collectstatic' == sys.argv[1]:
        DAJAXICE_MEDIA_PREFIX = 'website/dajaxice'
