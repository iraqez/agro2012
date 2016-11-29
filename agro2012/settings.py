import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qt++fg*-!xkrgj=u&y#onfom_4uczz-+^$5x@=vo$w&9jxd02-'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'agro2012.com.ua',
    'www.agro2012.com.ua',
    'dev.agro2012.com.ua',
    'www.dev.agro2012.com.ua',
]

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '.'))

# Application definition

INSTALLED_APPS = [
#    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_resized',
    'easy_thumbnails',
    'sorl.thumbnail',
    'image_cropping',
    'django_cleanup',
    'tinymce',

    'main',
    # 'employees',
    'office',
    'news',
]

IMAGE_CROPPING_SIZE_WARNING = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agro2012.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'agro2012.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     'NAME': 'agro2012',
#     'USER': 'postgres',
#     'PASSWORD': 'workfree',
#     'HOST': 'localhost', # Set to empty string for localhost.
#     'PORT': '5432', # Set to empty string for default.
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'uk-ua'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#обрезка фото
from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static',),
]

MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

IMAGE_CROPPING_THUMB_SIZE = (600, 600)
IMAGE_CROPPING_JQUERY_URL = 'js/jquery.min.js'
THUMBNAIL_DEBUG = True
HEADLESS = True

import autoslug
# using as many characters as needed to make a natural replacement
AUTOSLUG_SLUGIFY_FUNCTION = 'autoslug.utils.translit_long'

# using the minimum number of characters to make a replacement
AUTOSLUG_SLUGIFY_FUNCTION = 'autoslug.utils.translit_short'

# only performing single character replacements
AUTOSLUG_SLUGIFY_FUNCTION = 'autoslug.utils.translit_one'
# TEMPLATE_CONTEXT_PROCESSORS = (
#
# )
