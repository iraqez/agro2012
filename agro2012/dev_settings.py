from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     'NAME': 'dev-agro2012',
#     'USER': 'postgres',
#     'PASSWORD': 'workfree',
#     'HOST': 'localhost', # Set to empty string for localhost.
#     'PORT': '5432', # Set to empty string for default.
#     }
# }
