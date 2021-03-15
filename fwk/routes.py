from dataclasses import dataclass, field

import typing

from fwk.views import View


@dataclass
class Route:
    path: str
    view_cls: typing.Type[View]
    resource: str
    methods: typing.List[str] = field(default_factory=lambda: ["get"])
