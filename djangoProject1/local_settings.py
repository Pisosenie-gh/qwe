from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'meda(t5!+$%ecn0)^f85cp41jiies*qx&@8%2eix@x*hu6eb$*'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/static/',
]
