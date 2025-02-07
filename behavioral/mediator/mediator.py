from __future__ import annotations
from typing import List


# Interface do Mediador
class Mediator:
    def notify(self, sender: object, event: str) -> None:
        pass


# Implementação concreta do Mediador
class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator recebeu evento 'A'. Acionando Component2.")
            self._component2.do_c()
        elif event == "B":
            print("Mediator recebeu evento 'B'. Acionando Component1.")
            self._component1.do_a()


# Classe base para os componentes que usarão o Mediator
class BaseComponent:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator):
        self._mediator = mediator


# Componentes que comunicam via Mediator
class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component1 faz algo importante.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component1 faz outra coisa.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component2 responde ao evento 'A'.")

    def do_d(self) -> None:
        print("Component2 faz algo independente.")


# Uso do Mediator
component1 = Component1()
component2 = Component2()
mediator = ConcreteMediator(component1, component2)

print("\n🔹 Component1 dispara 'A':")
component1.do_a()

print("\n🔹 Component1 dispara 'B':")
component1.do_b()
