# -*- coding: utf-8 -*-

import os, socket

if socket.gethostname().startswith('gabriel'):
    LIVEHOST = False
else:
    LIVEHOST = True


PROJECT_ROOT = os.path.dirname(__file__)  

if LIVEHOST: 
    DEBUG = False
    TEMPLATE_DEBUG = DEBUG
else:
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

ADMINS = (
    #('Jérôme Beaulieu', 'jerome.beaulieu@trepantech.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'horizons_trep',      # Or path to database file if using sqlite3.
        'USER': 'horizons_trep',      # Not used with sqlite3.
        'PASSWORD': 'n3wtinmypants',     # Not used with sqlite3.
        'HOST': '',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': { 'init_command': 'SET storage_engine=MyISAM;' }
    }
}                                
EMAIL_HOST = 's3-singapore.accountservergroup.com'
EMAIL_PORT = '2525'
EMAIL_HOST_USER = "no-reply@horizonsprep.com"
EMAIL_HOST_PASSWORD = "7cy32]+c!i11"
EMAIL_USE_TLS=True


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
#STATIC_ROOT = os.path.join(PROJECT_ROOT)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'static/newhorizons'),
    os.path.join(PROJECT_ROOT, 'static/jquery'),

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y$uxkzuvg2vr371tpu9z!s!p7*6p$+!%(5oczvwkr_9(!szd^x'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "newhorizons.context_processors.site_settings",
    "newhorizons.context_processors.site_menu",
    "site_settings.context_processors.settings",
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

# Turn off in production

INTERNAL_IPS=('127.0.0.1',)
ADMIN_LANGUAGE_CODE = 'en'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Enabling translation
    'django.middleware.locale.LocaleMiddleware',
    'newhorizons.custom_middleware.AdminLocaleURLMiddleware',
)

if not LIVEHOST:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

ROOT_URLCONF = 'newhorizons.urls'

# For i18n localization
LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'locale'),
    #'/locale/',
)
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('zh-cn', gettext('Chinese')),
    ('ko', gettext('Korean')),
)
DEFAULT_LANGUAGE = 'en'

# Settings for TinyMCE
DJANGO_SETTINGS_MODULE='testtinymce.staticfiles_settings'
TINYMCE_JS_URL = (os.path.join(STATIC_URL, 'scripts/tiny_mce/tiny_mce.js'))
TINY_MCE_JS_ROOT = (os.path.join(STATIC_ROOT, 'scripts/tiny_mce/tiny_mce.js'))
#TINY_MCE_DEFAULT_CONFIG
#TINYMCE_COMPRESSOR = True 
#TINYMCE_FILEBROWSER = False
TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'paste', 
    'theme': 'advanced',
    'convert_urls': 'false',
}
TINYMCE_SPELLCHECKER = True

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'newhorizons.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'template'),
)

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south', # Schema and data migration project for Django
    'node',
    'advert',
    'banner',
    'blog',
    'course',
    'instructor',
    'inthenews',
    'location',
    'news',
    'page',
    'siteimage',
    'sitemessage',
    'site_settings',
    'testimonial',
    'tinymce',
)

if not LIVEHOST:
    INSTALLED_APPS += ('debug_toolbar',)

# Grappelli settings (custom backend)
GRAPPELLI_ADMIN_TITLE = 'New Horizons'
AUTOCOMPLETE_LIMIT = '8'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': PROJECT_ROOT + "/logfile",
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
