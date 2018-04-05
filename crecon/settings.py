# -*- coding: utf-8 -*-
"""
Django settings for crecon project.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2*_)ma(s6ggon16#lttsuo2)10w@8z-yuv@%+62#^8$@ggijk('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

NEED_REGENERATE_MODELS = ['Page', ]


ADMINS = (
    ('admin', 'admin@gmail.com'),
)

# Application definition

INSTALLED_APPS = (
#    'grappelli',
#    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'raven.contrib.django.raven_compat',

    # 'south',

    # 'mptt',
    # 'mpttadmin',

    # 'tinymce',

    'bootstrap3',
    'crecon.apps.CreconConfig',

    ###===user-generated-apps===###
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'crecon/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


ROOT_URLCONF = 'crecon.urls'

WSGI_APPLICATION = 'crecon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': '{{ crecon }}',          # Or path to database file if using sqlite3.
#         'USER': 'root',                        # Not used with sqlite3.
#         'PASSWORD': 'changeme',                  # Not used with sqlite3.
#         'HOST': '82.151.212.181',                # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '3306',                        # Set to empty string for default. Not used with sqlite3.
#         'TEST_CHARSET': 'utf8',
#         'TEST_COLLATION': 'utf8_general_ci',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'crecon/public/media')
MEDIA_URL = '/media/'


STATIC_ROOT = os.path.join(BASE_DIR, 'crecon/public/static')
STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "crecon/static"),
)


# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR, 'crecon/templates'),
# )


if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


NO_IMG_PATH = 'no_img.png'


TINYMCE_DEFAULT_CONFIG = {
    'plugins': "safari,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",
    'theme': "advanced",
    'theme_advanced_buttons1': "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,|,styleselect,formatselect",
    'theme_advanced_buttons2': "cut,copy,paste,pasteword,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,code,|,forecolor,backcolor",
    'theme_advanced_buttons3': "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,iespell,media,advhr,|,fullscreen",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': "true",
    'relative_urls': False,
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'loginza.authentication.LoginzaBackend',
)

FACEBOOK_APP_ID = '540390736294908'
FACEBOOK_API_SECRET = '08358f663e44f11cc3abd203c8bc0890'
