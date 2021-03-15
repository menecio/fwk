import typing

from fwk.exceptions import MethodNotAllowed
from fwk.requests import Request


class View:
    request: typing.Optional[Request] = None

    async def dispatch(self, scope, receive, send):
        self.request = Request(scope, receive)

        try:
            method = getattr(self, self.request.method)
        except AttributeError:
            raise Exception("Method not supported")

        response = await method(self.request)
        await response(send)

    async def head(self, request: Request, *args, **kwargs):
        raise MethodNotAllowed

    async def options(self, request: Request, *args, **kwargs):
        raise MethodNotAllowed

    async def get(self, request: Request, *args, **kwargs):
        raise MethodNotAllowed

    async def post(self, request: Request, *args, **kwargs):
        raise MethodNotAllowed

    async def put(self, request: Request, *args, **kwargs):
        raise MethodNotAllowed

    async def patch(self, request: Request, *args, **kwargs):
        raise MethodNotAllowed

    async def delete(self, request: Request, *args, **kwargs):
        raise MethodNotAllowed
