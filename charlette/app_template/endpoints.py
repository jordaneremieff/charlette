from starlette.applications import Starlette

from charlette.endpoints import TemplateEndpoint


{{app_name}} = Starlette()


@{{app_name}}.route("/")
class DefaultEndpoint(TemplateEndpoint):
    template_name = "index.html"
    context = {"welcome": "Hello, Charlette!"}
