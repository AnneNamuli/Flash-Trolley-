"""
Django settings for GroupOne project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ln8(&1z&qod)x=!*p1f6q)*%z0ukwc7lhr)+3)3aa7_ha@)hw_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'flashTrolley',
    'social.apps.django_app.default',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'GroupOne.urls'

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
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',

                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)


WSGI_APPLICATION = 'GroupOne.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'flashTrolley.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIR = (os.path.join(BASE_DIR, 'static/'), BASE_DIR)

ADMIN_SITE_HEADER = "Flash-Trolley administration"
LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '1681300888748079'
SOCIAL_AUTH_FACEBOOK_SECRET = 'e7bb717159df86cfb7b4109625d429bc'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1067151963820-0pc08n0rt3mn3nc8euattrmjllbn9eh9.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'R-grdsKQ4DVZOXRHWVKVE4Qj'
SOCIAL_AUTH_TWITTER_KEY = 'OEQdmJMQTO7N5DjpslTdhzc0w'
SOCIAL_AUTH_TWITTER_SECRET = 'ANFTrF5xoSrCRdCULJDNoxqYiMbywUy0pD0uxwSMAeFscFZh1A'

MEDIA_ROOT = PROJECT_ROOT
MEDIA_URL = '/media/'

