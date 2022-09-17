from .base import *


DEBUG = True

ALLOWED_HOSTS = ['mercadooweb.herokuapp.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dr3frth5osr13',
        'USER': 'rhzfmyreoybvlj',
        'PASSWORD': 'aab00fb6edfc3ee3393199aea1e3d9478c9871f1eb94ddafb83060b919e9cf6f',
        'HOST': 'ec2-52-200-5-135.compute-1.amazonaws.com',
        'PORT': '5432',
    }

}

STATICFILES_DIRS = (BASE_DIR,'static')