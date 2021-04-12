from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['librarydjango21.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'da5ve3o71k7e5n',
        'USER': 'njsweouplnxrbp',
        'PASSWORD': '0b9432b2275238b6b4a711655f25afc0e3e70ef67b4bc7c77324413e72150147',
        'HOST': 'ec2-18-206-20-102.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}
