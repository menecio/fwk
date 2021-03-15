import typing
from dataclasses import dataclass, field

from routes import Mapper

from fwk.exceptions import HTTPError, NotFoundError, exception_handler
from fwk.routes import Route


@dataclass
class Application:
    name: str
    middleware: typing.List[typing.Callable] = field(default_factory=list)
    routes: typing.List[Route] = field(default_factory=list)
    debug: bool = False
    exception_handler: typing.Callable = field(default=exception_handler)

    def __post_init__(self):
        self._map = Mapper(controller_scan=False)
        for route in self.routes:
            self._map.connect(self.name, route.path, controller=route.view_cls)
            self._map.create_regs()

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            raise Exception(f"'{scope['type']}' protocol is not supported")

        try:
            route = self._map.match(scope["path"])
            if route is None:
                raise NotFoundError
            view = route["controller"]()
            await view.dispatch(scope, receive, send)
        except HTTPError as error:
            await self.exception_handler(send, error)
