from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'library',
        'USER': 'denis',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '5432'
    }
}
