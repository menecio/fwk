from dataclasses import dataclass
from http import HTTPStatus

from fwk.responses import Response


@dataclass
class HTTPError(Exception):
    status: HTTPStatus

    def as_dict(self):
        return {
            "status": self.status.value,
            "error": self.status.phrase,
            "description": self.status.description,
        }

    @property
    def status_code(self):
        return self.status.value

    @property
    def description(self):
        return self.status.description


@dataclass
class NotFoundError(HTTPError):
    status: HTTPStatus = HTTPStatus.NOT_FOUND


@dataclass
class MethodNotAllowed(HTTPError):
    status: HTTPStatus = HTTPStatus.METHOD_NOT_ALLOWED


async def exception_handler(send, error: HTTPError):
    response = Response(error.status_code, error.description)
    await response(send)
