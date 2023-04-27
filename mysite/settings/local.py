from .base import * 
ALLOWED_HOSTS = ['*','0.0.0.0']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pybo',
        'USER' : 'root',
        'PASSWORD' : '1234',
        'HOST' : 'mysql',
        'PORT' : '4000'
    }
}

INSTALLED_APPS.append("django_extensions")
