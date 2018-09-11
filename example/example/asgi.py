import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")
django.setup()
application = get_default_application()
