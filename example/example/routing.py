from starlette.applications import Starlette

from myapp.endpoints import myapp

application = Starlette(debug=True)
application.mount("/myapp", myapp)
