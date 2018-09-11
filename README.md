# charlette

Charlette is a reusable Django app that provides a simple means of configuring a [Channels](https://channels.readthedocs.io/en/latest/)-enabled project to use components from the [ASGI](https://asgi.readthedocs.io/en/latest/) library [Starlette](https://www.starlette.io). 

It is intended to demonstrate the composability of ASGI applications.

**Requirements**: Python 3.6+

## Setup

- `pip3 install charlette`

- Create a project, `example`, with the command: `charlette startproject <projectname>`. This will generate a Django project with Charlette's configuration.

- Create an app, `myapp`, with the command: `charlette startapp myapp`. This will generate a boilerplate app that uses Starlette's application class and a custom `TemplateEndpoint` provided by Charlette.

- Add the app to the `INSTALLED_APPS` in the Django `settings.py` file:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    ...
    "myapp",
    ...
    "charlette",
    "channels",
]
```

- Import the app in the `routing.py` file and mount it to the main Starlette application.

```python
from starlette.applications import Starlette

from myapp.endpoints import myapp

application = Starlette(debug=True)
application.mount("/myapp", myapp)
```

- Navigate to `http://localhost:8000/myapp/` in your browser.
