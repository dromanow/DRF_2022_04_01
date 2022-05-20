from .debug import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'library',
        'USER': 'denis',
        'PASSWORD': 'qwerty',
        'HOST': '127.0.0.1',
        'PORT': '54327'
    }
}
