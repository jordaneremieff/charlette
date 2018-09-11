from starlette.endpoints import HTTPEndpoint

from charlette.utils import render_response


class TemplateEndpoint(HTTPEndpoint):

    template_name = None
    context_data = {}

    def get(self, request):
        return render_response(self.template_name, context=self.context)
