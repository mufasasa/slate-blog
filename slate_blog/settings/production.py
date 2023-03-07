from .base import *
import dj_database_url

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    'default': dj_database_url.parse("postgresql://slate_blog:AVNS_qsIEujR4hnyYewnP_IZ@slate-pgres-do-user-464771-0.b.db.ondigitalocean.com:25060/slate_blog?sslmode=require")
}

ALLOWED_HOSTS = ["*"]