from .base import *
import dj_database_url

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'slate_blog',
        'USER': 'slate_blog',
        'PASSWORD': 'slate_blog',
        'HOST': 'localhost',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ["*"]