from pydantic import BaseModel
from abc import abstractmethod, ABC
from typing import Self, Literal


class Pizza(BaseModel):
    tamanho: Literal["Média", "Pequena", "Grande"] | None = None
    tipo: Literal["Fina", "Tradicional", "Grossa"] | None = None
    sabor: str = None
    borda: Literal["Catupry", "Cheddar", "Sem Borda"] | None = None
    extra: list[str] = None


class IPizzaBuilder(ABC):
    def __init__(self) -> None:
        self.pizza = Pizza()

    @property
    @abstractmethod
    def result(self) -> Pizza:
        pass

    @abstractmethod
    def add_tamanho(self, tamanho: str) -> Self:
        pass

    @abstractmethod
    def add_tipo(self, tipo: str) -> Self:
        pass

    @abstractmethod
    def add_sabor(self, sabor: str) -> Self:
        pass

    @abstractmethod
    def add_borda(self, borda: str) -> Self:
        pass

    @abstractmethod
    def add_extra(self, extra: list[str]) -> Self:
        pass


class ConcretePizzaBuilder(IPizzaBuilder):
    @property
    def result(self) -> Pizza:
        return self.pizza

    def add_tamanho(self, tamanho: str) -> IPizzaBuilder:
        self.pizza.tamanho = tamanho
        return self

    def add_tipo(self, tipo: str) -> IPizzaBuilder:
        self.pizza.tipo = tipo
        return self

    def add_sabor(self, sabor: str) -> IPizzaBuilder:
        self.pizza.sabor = sabor
        return self

    def add_borda(self, borda: str) -> IPizzaBuilder:
        self.pizza.borda = borda
        return self

    def add_extra(self, extra: list[str]) -> IPizzaBuilder:
        self.pizza.extra = extra
        return self


class PizzaDirector:
    def __init__(self, pizza_builder: ConcretePizzaBuilder) -> None:
        self.pizza_builder = pizza_builder

    def small_pattern(self, sabor: str) -> Pizza:
        self.pizza_builder.add_tamanho("pequena").add_borda("Sem borda").add_sabor(
            sabor
        ).add_tipo("Tradicional")
        return self.pizza_builder.result


pizza_builder = ConcretePizzaBuilder()
pizza_director = PizzaDirector(pizza_builder)

pizza = pizza_director.small_pattern("Frango")

