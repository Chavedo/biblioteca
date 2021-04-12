from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['librarydjango21.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'biblioteca',
        'USER': 'root',
        'PASSWORD': '789456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
