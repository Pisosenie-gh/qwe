

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'meda(t5!+$%ecn0)^f85cp41jiies*qx&@8%2eix@x*hu6eb$*'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'asocation',
        'USER': 'userdb',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/static/',
]


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
