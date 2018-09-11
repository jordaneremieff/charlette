from django.template.loader import get_template

from starlette.responses import HTMLResponse


def render_response(template_name, response_class=HTMLResponse, context={}):
    template = get_template(template_name)
    rendered = template.render(context)
    return response_class(rendered)
