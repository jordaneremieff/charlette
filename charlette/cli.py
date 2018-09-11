import os

from django.core import management
from innate import Innate
from charlette.__version__ import __version__

innate = Innate(description=f"Charlette v{__version__}")


TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_TEMPLATE = os.path.join(TEMPLATE_DIR, "project_template")
APP_TEMPLATE = os.path.join(TEMPLATE_DIR, "app_template")


@innate()
def startproject(name):
    """Create a new Django project with Charlette's settings."""
    management.call_command("startproject", name, template=PROJECT_TEMPLATE)


@innate()
def startapp(name):
    """Create a new Django app with Charlette's settings."""
    management.call_command("startapp", name, template=APP_TEMPLATE)
