from dataclasses import dataclass
from http import HTTPStatus


@dataclass
class Response:
    status: int = HTTPStatus.NO_CONTENT
    body: str = ""
    content_type: str = "text/plain"

    async def __call__(self, send):
        await send({
            'type': 'http.response.start',
            'status': self.status,
            'headers': [
                (b'content-type', self.content_type.encode("utf-8")),
                (b'content-length', str(len(self.body.encode("utf-8"))).encode("utf-8")),
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': self.body.encode("utf-8"),
        })
