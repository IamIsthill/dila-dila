"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

import environ

env = environ.Env()
environ.Env.read_env(env_file='.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7_&xaz^@5w92#^v8@7-=fz7k)0d0eqgeelxqqpm$$495#3ua&-"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("LOCAL_DEV", False)

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
   
    "base.apps.BaseConfig",
    "users.apps.UsersConfig",
    "patients.apps.PatientsConfig",
    "medicine_request.apps.MedicineRequestConfig",
    "records.apps.RecordsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # for serving static files in production
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
          BASE_DIR/'templates',
        ],
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

WSGI_APPLICATION = "app.wsgi.application"
ASGI_APPLICATION = "app.asgi.application"


# Render Postgre DB Live
import dj_database_url


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "HOST": env("DATABASE_HOST"),
        "PORT": 6543,
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Manila"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
  BASE_DIR / 'static'
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
        os.path.join(BASE_DIR, 'node_modules')
    ]

AUTH_USER_MODEL="users.User"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587  
EMAIL_USE_TLS = True 
EMAIL_HOST_USER = env('EMAIL_ADD') 
EMAIL_HOST_PASSWORD = env('EMAIL_PASS') 

# # AWS CONFIG
# AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY")

# AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    ALLOWED_HOSTS = [
        'local-hrms.duckdns.org', 
        'http://local-hrms.duckdns.org', 
        'https://local-hrms.duckdns.org',
        '35.197.90.138',
        '127.0.0.1:8000',
        '127.0.0.1',
        'http://127.0.0.1:8000',
        'http://127.0.0.1',
    ]
    CSRF_TRUSTED_ORIGINS = [
        'https://local-hrms.duckdns.org',
        'http://local-hrms.duckdns.org',
        'http://127.0.0.1:8000',
    ]

# New config
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_SAVE_EVERY_REQUEST = True

if env.bool("LOCAL_DEV", False):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

