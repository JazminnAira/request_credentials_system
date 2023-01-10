# THIS SETUP IS APPLICABLE VIA ONLINE ONLY, USE LOCAL __INIT__ IF NEEDED

"""
Django settings for gradclear_project project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-66yny&_e3kz@(3nux544d*spq7e&@9hbqo7j&gd4d&qv!ry^gw'

# SECURITY WARNING: don't run with debug turned on in production!
# SET TO FALSE FOR SECURITY PURPOSES
DEBUG = True

ALLOWED_HOSTS = ['tupcaviteregistrar.site', 'www.tupcaviteregistrar.site']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gradclear_app',
    'django_crontab',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gradclear_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


WSGI_APPLICATION = 'gradclear_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tupclget_gradclear_database',
        'USER': 'tupclget_root',
        'PASSWORD': 'chimkenflet2022',
        'HOST': 'localhost', 
        'PORT': '3306',
        'OPTIONS': {"init_command": "SET foreign_key_checks = 0;",},

    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = '/static/'
MEDIA_URL = '/Media/'
MEDIA_ROOT = '/home/tupclget/public_html/Media'
# STATIC_ROOT = 'gradclear_project/gradclear_app/static'

# STATICFILES_DIRS = [os. path.join(BASE_DIR, 'static')]

# deployment
STATIC_URL = '/static/'
STATIC_ROOT = '/home/tupclget/public_html/static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'gradclear_app.user_table'

# FOR EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tupc.registrar.office@gmail.com'
EMAIL_HOST_PASSWORD = 'csvhjdbhjeenhmgq'
 
# EMAIL_USE_SSL= False
# EMAIL_TIMEOUT= None
# EMAIL_SSL_KEYFILE= None
# EMAIL_SSL_CERTIFILE= None

# EMAIL_BACKEND = 'django.core.mail.backends. .EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
# EMAIL_FILE_PATH = '/tmp/app-messages' 

# EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True     # LOGOUT WHEN BROWSER IS CLOSED
# SESSION_COOKIE_AGE = 1800                  # 30 MINS INACTIVITY, AUTO LOGOUT
SESSION_SAVE_EVERY_REQUEST = True          # Will prevent from logging you out after 300 seconds
 

# SET TO WEEKDAYS AT 3 AM IN THE MORNING BASED ON EST
# BASED ON EST SINCE SERVER IS IN US
# AUTOMATICALLY CONVERTED TO GMT 800, NO ITERATIONS REQUIRED
CRONJOBS = [
    ('0 3 * * 1-5', 'gradclear_app.cron.my_scheduled_job')
]