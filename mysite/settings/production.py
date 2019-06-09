from .base import *
import environ
import dj_database_url

env = environ.Env()
DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'blog/static')
LOGIN_REDIRECT_URL = '/'
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangogirls',
        'USER': 'postgres',
        'PASSWORD': 'anowataru',
        'HOST': 'localhost',
        'PORT': '',
    }
}

AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')
