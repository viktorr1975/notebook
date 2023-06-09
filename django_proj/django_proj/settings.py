"""
Django settings for django_proj project.

Generated by 'django-admin startproject' using Django 4.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
# import os
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-s@6v4=xgd(f020eu-4!fbzda5@vor2fw()@udn$044@86$!1#6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "bootstrap5",
    "rest_framework",
    "myapp",
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

ROOT_URLCONF = "django_proj.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        #        'DIRS': [],
        "DIRS": [os.path.join(BASE_DIR, "templates")],  # для шаблонов login/logout
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

WSGI_APPLICATION = "django_proj.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_db",
        "USER": "postgres",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "",
        "TEST": {
            "NAME": "mytestdatabase",
        },
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

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# https://docs.djangoproject.com/en/4.1/ref/settings/#static-files
STATIC_URL = "/static/"
# STATIC_ROOT='/'            #The absolute path to the directory where collectstatic will collect static files for deployment.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# DRF
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
# -------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        #        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",  # работает только в режиме DEBUG
        "rest_framework.authentication.SessionAuthentication",
    ],
    # "DEFAULT_RENDERER_CLASSES": [
    #     "rest_framework.renderers.JSONRenderer",
    # ],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.openapi.AutoSchema",
    #
    # "DEFAULT_FILTER_BACKENDS": [
    #     "django_filters.rest_framework.DjangoFilterBackend",
    #     "rest_framework.filters.SearchFilter",
    #     "rest_framework.filters.OrderingFilter",
    # ],
    "ORDERING_PARAM": "ordering",
    # "TEST_REQUEST_DEFAULT_FORMAT": "json",
    # "DEFAULT_PAGINATION_CLASS": "articles.pagination.BasePageNumberPagination",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    # # "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

# System logging
# loggin reference - https://docs.djangoproject.com/en/4.1/ref/logging/#logging-ref
# -------------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s "},
        # 'django.server': {
        #     '()': 'django.utils.log.ServerFormatter',
        #     'format': '[{server_time}] {message} {pathname} {funcName}',
        #     'style': '{',
        # }
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}:{message}] {request}",
            "style": "{",
        },
    },
    "handlers": {  # куда передовать сообщиния
        "console": {
            "class": "logging.StreamHandler",  # сообщения передаём в консоль
            "level": "INFO",  # сообщения уровня INFO, WARNING, ERROR, CRITICAL передаём
        },
        "django.server": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        # use this handler to swallow all logging - this is the nuclear option
        "null": {
            "level": "DEBUG",
            "class": "logging.NullHandler",
        },
    },
    # 'formatters': {
    #     'simple': {
    #         'format': '[%(asctime)s] %(levelname)s %(message)s',
    #         'datefmt': '%Y-%m-%d %H:%M:%S'
    #     },
    #     'verbose': {
    #         'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
    #         'datefmt': '%Y-%m-%d %H:%M:%S'
    #     },
    # },
    "loggers": {
        "django.server": {  #  Log messages related to the handling of requests received by the server invoked by the runserver command.
            "handlers": ["django.server"],  # handler
            "level": "INFO",  # сообщения уровня INFO, WARNING, ERROR, CRITICAL передаём
            "propagate": False,  # не передовать сообщиния дальше по иерархии сборщиков сообщений
        },
    },
}

# Whether to append trailing slashes to URLs.
APPEND_SLASH = False

# use a custom user model
AUTH_USER_MODEL = "myapp.CustomUser"

# Пользователи будут перенаправлены на главную страницу после входа в систему
LOGIN_REDIRECT_URL = "home"
# перенаправит пользователей обратно на главную страницу, как только они выйдут из системы
LOGOUT_REDIRECT_URL = "login"
