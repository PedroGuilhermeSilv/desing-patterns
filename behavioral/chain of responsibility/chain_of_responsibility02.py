from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Request:
    value: float

@dataclass
class Response:
    result: bool


class Handler(ABC):
    def __init__(self, nextHandler: Handler | None) -> None:
        self.nextHandler = nextHandler

    @abstractmethod
    def handle(request: Request) -> Response:
        pass


class Supervisor(Handler):
    def handle(self, request: Request) -> Response:
        if request.value <= 100:
            print(f"valor aprovado pelo supervisor:{request.value}")
            return Response(True)
        return self.nextHandler.handle(request)


class Gerente(Handler):
    def handle(self, request: Request) -> Response:
        if request.value > 100 and request.value <= 1000:
            print(f"valor aprovado pelo gerente:{request.value}")
            return Response(True)
        return self.nextHandler.handle(request)


class Diretor(Handler):
    def handle(self, request: Request) -> Response:
        if request.value > 1000:
            print(f"valor aprovado pelo diretor:{request.value}")
            return Response(True)
        return self.nextHandler.handle(request)


diretor = Diretor(None)
gerent = Gerente(diretor)
supervisor = Supervisor(gerent)

supervisor.handle(Request(1200))
