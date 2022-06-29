from settings import SETTINGS

INSTALLED_APPS = []

SECRET_KEY = 'REPLACE_ME'
USE_TZ = True
TIME_ZONE = "Australia/Sydney"
DEFAULT_AUTO_FIELD ='django.db.models.BigAutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django_project.mysql_engine',  # necessary to avoid disconnects
        'NAME': SETTINGS.db_name,
        'USER': SETTINGS.db_user,
        'PASSWORD': SETTINGS.db_pass,
        'HOST': SETTINGS.db_host,
        'PORT': '3306',
    }
}

INSTALLED_APPS = [
    "django_project.apps.example"
]
