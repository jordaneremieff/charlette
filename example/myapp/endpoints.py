from starlette.applications import Starlette

from charlette.endpoints import TemplateEndpoint


myapp = Starlette()


@myapp.route("/")
class DefaultEndpoint(TemplateEndpoint):
    template_name = "index.html"
    context = {"welcome": "Hello, Charlette!"}
