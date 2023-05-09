from .base import * 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pybo',
        'USER' : 'encore',
        'PASSWORD' : 'encore!@#',
        'HOST' : '3.38.101.98',
        'PORT' : '3306'
    }
}
INSTALLED_APPS.append("django_extensions")
