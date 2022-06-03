from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['secret-forest-35723.herokuapp.com', '*','entreaceros.com.ar','entre-aceros.herokuapp.com']
CSRF_TRUSTED_ORIGINS = ['https://entreaceros.com.ar']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
