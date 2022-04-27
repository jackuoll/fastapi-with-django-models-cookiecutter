# fastapi-with-django-models-cookiecutter

Barebones project for FastAPI with Django models


## Running Web

Included is a template for for a Hello World endpoint at `/web/__init__.py`

To run a development server:

```bash
uvicorn web:app --reload
```

## Using Models

You can create and use models the same way you would in a normal Django project, however you'll need to setup Django when importing them.

```python
import logging
import os

from django.db import models
import django

try:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_settings")
    django.setup()
    logging.info("Setting up django models..")
except RuntimeError:
    pass


class MyModel(models.Model):
    name = models.CharField()
```

## Using MySQL
Django with MySQL has an issue with persistent connections when not used in the normal django request context - connections are never refreshed so once the server connection timeout has expired, connections will begin to fail. Included in this project is a custom MySQL DB wrapper that will reconnect when the connection is lost. To use it:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django-project.db_engines.mysql_engine',  # necessary to avoid disconnects
        'NAME': SETTINGS.db_name,
        'USER': SETTINGS.db_user,
        'PASSWORD': SETTINGS.db_pass,
        'HOST': SETTINGS.db_host,
        'PORT': '3306',
    }
}
```


## Settings

Settings can be managed by a .env file and the root `settings.py`. Any variable set in settings can be overridden by the .env file by simply placing a variable with the same name in the .env file.

eg:
```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    my_compulsary_variable: str
    my_variable_with_default: str = "my default"
    another_variable_with_default: str = "another default"

    
SETTINGS = Settings()
```

```dotenv
.env

my_compulsary_variable="Hello World"
my_variable_with_default="Changed"
```
With the above setup, the values in SETTINGS will be:
* `my_compulsary_variable="Hello World"`
* `my_variable_with_default="Changed"`
* `another_variable_with_default="another default"`

Django settings can now import `SETTINGS` so you do not need to handle reading environment variables yourself.

For more information, see [Pydantic BaseSettings](https://pydantic-docs.helpmanual.io/usage/settings/).
