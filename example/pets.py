from fwk.applications import Application
from fwk.requests import Request
from fwk.responses import Response
from fwk.routes import Route
from fwk.views import View


class HelloView(View):
    async def get(self, request: Request, *args, **kwargs):
        return Response(status=200, body="Pets!")


app = Application("Pets", routes=[Route("/hello", view_cls=HelloView, resource="home")])
