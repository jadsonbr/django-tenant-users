"""
Django settings for test_tenant_schemas project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@7m&5-ez*y7ft%kft)n#9^n#h%wj(*1qlhuc#xms^5wobv*=)l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

SHARED_APPS = (
    'tenant_schemas',  # Use django-tenant-schemas
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tenant_users.permissions',
    'tenant_users.tenants',
    'test_tenant_schemas.companies',
    'test_tenant_schemas.users',
)

TENANT_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'tenant_users.permissions',
)

INSTALLED_APPS = list(SHARED_APPS) + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]


# tenant-schemas configuration
TENANT_MODEL = 'companies.Company'
DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'
PUBLIC_SCHEMA_NAME = 'public'

# django-tenant-users configuration
AUTH_USER_MODEL = 'users.TenantUser'
TENANT_USERS_DOMAIN = 'test.com'
AUTHENTICATION_BACKENDS = ('tenant_users.permissions.backend.UserBackend',)


MIDDLEWARE = [
    'tenant_schemas.middleware.TenantMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_tenant_schemas.test_tenant_schemas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'test_tenant_schemas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'tenant_schemas.postgresql_backend',
        'USER': os.environ.get('DJANGO_DATABASE_USER', default=''),
        'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD', default=''),
        'NAME': os.environ.get('DJANGO_DATABASE_NAME', default=''),
        'PORT': os.environ.get('DJANGO_DATABASE_PORT', default=''),
        'HOST': os.environ.get('DJANGO_DATABASE_HOST', default=''),
    },
}

DATABASE_ROUTERS = ('tenant_schemas.routers.TenantSyncRouter',)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
