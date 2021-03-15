from dataclasses import dataclass, field

from hypercorn.typing import Scope


@dataclass
class Request:
    scope: Scope = field(init=True)
    receive: "Receive" = field(init=True)

    @property
    def headers(self):
        return self.scope["headers"]

    @property
    def method(self):
        return self.scope["method"].lower()

    @property
    def path(self):
        return self.scope["path"]

    @property
    def query(self):
        return self.scope["query_string"]
