"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n&de6$-$c0*p^0fznh=h!xx2gd-=2_)s*^t__!!@h03l#$-syy'
2
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = [*]


# Application definition

INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'embed_video',
    'rest_framework',
    'reset_migrations',
    'rest_framework.authtoken',
    # 'crispy_forms',
    # 'django_cleanup',
    # 'background_task',
    # 'organizations',
    # 'phone_login',
    'django_cron',
    'django_celery_beat',
    'django_celery_results',
    'corsheaders',
    # 'django_celery',
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
                'rest_framework.permissions.IsAuthenticated',
                'rest_framework.permissions.AllowAny',
    ],
}

# 'DEFAULT_PERMISSION_CLASSES': [
#    'rest_framework.permissions.AllowAny',
# ]

# AUTHENTICATION_BACKENDS = [
#     'phone_login.backends.phone_backend.PhoneBackend',
#     # 'django.contrib.auth.backends.ModelBackend',
# ]


from celery import Celery

celery = Celery(broker="amqp://guest:guest@127.0.0.1:5672//")

celery.conf.update(
    CELERY_DEFAULT_QUEUE = "myapp",
    CELERY_DEFAULT_EXCHANGE = "myapp",
    CELERY_DEFAULT_EXCHANGE_TYPE = "direct",
    CELERY_DEFAULT_ROUTING_KEY = "myapp",
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'genorion',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
    }
}

# DATABASES = {
#     'default':{
#         'ENGINE': 'django,db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
#     }
# }
# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

# AUTH_USER_MODEL = 'myapp.User'


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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

TIME_INPUT_FORMATS = ('%H:%M',)

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL='/media/'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
#Activate Django-Heroku.
django_heroku.settings(locals())

# AUTH_USER_MODEL = 'myapp.User'

SESSION_COOKIE_AGE = 3600
GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = '<https://drive.google.com/file/d/1k7RdoldvQNs_bHBnKeptQ773Mqs_qVw0/view?usp=sharing>'

# sid: ACd6173a93be390fe7eb1f2bf7faceeb0e
# token: 4892323294c8cc241e2107380b0c3f59
# number : +12095887091

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'spaceorion2021@gmail.com'
EMAIL_HOST_PASSWORD = 'space@2020@'