from .base import * 
ALLOWED_HOSTS = ['*','0.0.0.0']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pybo',
        'USER' : 'encore',
        'PASSWORD' : 'encore!@#',
        'HOST' : '3.38.101.98', 
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"'
        }
    }
}

INSTALLED_APPS.append("django_extensions")
