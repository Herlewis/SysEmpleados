from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '35xrekp%_x*c8gysdhm7a@x1l9x5ug!^fni-=x#vqf#0ai7=v!'


ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbbiblioteca',
        'USER': 'herlewis',
        'PASSWORD': 'herlewis',
        'HOST':'localhost',
        'PORT':'5432',
    }
}





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'