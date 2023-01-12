"""
Django settings for ecommerce_poc project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import json
import os
from decouple import config as dev_config

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG == False:
  pass
else:
  with open('/etc/ecommerce_config.json') as config_file:
    config = json.load(config_file)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG == False:
  SECRET_KEY = dev_config("DJANGO_SECRET_KEY")
else:
  SECRET_KEY = config["DJANGO_SECRET_KEY"]

ALLOWED_HOSTS = [ '3.89.21.130', 'localhost', 'ecommerce.sauerwebdev.com' ]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ecommerce",
    'fontawesomefree',
    'django_extensions',
    'polymorphic',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ecommerce_poc.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ecommerce_poc.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if DEBUG == False:
  DATABASES = {
      'default': {
          'ENGINE' : dev_config("DB_ENGINE"),
          'NAME': dev_config("DB_NAME"),
          'USER': dev_config("DB_USER"),
          'PASSWORD': dev_config("DB_PASS"),
          'HOST': dev_config("DB_HOST"),
          'PORT': dev_config("DB_PORT"),
      }
  }

else:
  DATABASES = {
      'default': {
          'ENGINE' : config["DB_ENGINE"],
          'NAME': config["DB_NAME"],
          'USER': config["DB_USER"],
          'PASSWORD': config["DB_PASS"],
          'HOST': config["DB_HOST"],
          'PORT': config["DB_PORT"],
      }
  }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

if DEBUG == False:

  AWS_ACCESS_KEY_ID = dev_config("AWS_ACCESS_KEY_ID")
  AWS_SECRET_ACCESS_KEY = dev_config("AWS_SECRET_ACCESS_KEY")
  AWS_STORAGE_BUCKET_NAME = dev_config("AWS_STORAGE_BUCKET_NAME")
  AWS_LOCATION = dev_config("AWS_LOCATION")
  STATIC_ROOT = dev_config("AWS_LOCATION")
else:
  AWS_ACCESS_KEY_ID = config["AWS_ACCESS_KEY_ID"]
  AWS_SECRET_ACCESS_KEY = config["AWS_SECRET_ACCESS_KEY"]
  AWS_STORAGE_BUCKET_NAME = config["AWS_STORAGE_BUCKET_NAME"]
  AWS_LOCATION = config["AWS_LOCATION"]
  STATIC_ROOT = config["AWS_LOCATION"]

AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/ecomm'

# we are temporarily using this so that the password reset link
# that is supposed to be sent via email is actually just printed to the
# console so we can copy and paste. we can use the following link to the django docs
# to set up this reset link being sent to a user's actual email:
# https://docs.djangoproject.com/en/4.0/topics/email/
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if DEBUG == False:
  # stripe api keys
  STRIPE_PUBLIC_KEY = dev_config("STRIPE_PUBLIC_KEY")
  STRIPE_SECRET_KEY = dev_config("STRIPE_SECRET_KEY")
  SENDGRID_API_KEY = dev_config("SENDGRID_API_KEY")
  DEFAULT_FROM_EMAIL = dev_config("FROM_EMAIL")
else:
  # stripe api keys
  STRIPE_PUBLIC_KEY = config["STRIPE_PUBLIC_KEY"]
  STRIPE_SECRET_KEY = config["STRIPE_SECRET_KEY"]
  SENDGRID_API_KEY = config["SENDGRID_API_KEY"]
  DEFAULT_FROM_EMAIL = config["FROM_EMAIL"]

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # Exactly that. 
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587 # 25 or 587 (for unencrypted/TLS connections).
EMAIL_USE_TLS = True

SENDGRID_SANDBOX_MODE_IN_DEBUG = False