### Uma classe filha deve poder ser substituída pela suas classe pai."

# Má implementação - Violando LSP
class Bird:
    def fly(self):
        print("Voando...")


class Duck(Bird):
    def fly(self):
        print("Pato voando...")

    def swim(self):
        print("Pato nadando...")


class Penguin(Bird):  # Viola LSP porque pinguim não pode voar!
    def fly(self):
        raise NotImplementedError(
            "Pinguins não podem voar!"
        )  # Quebra o comportamento esperado

    def swim(self):
        print("Pinguim nadando...")


# Boa implementação - Seguindo LSP
from abc import ABC, abstractmethod


class Bird(ABC):
    @abstractmethod
    def fly(self): ...

class BirdSwin(ABC):
    @abstractmethod
    def swin(self): ...


class Duck(Bird):
    def fly(self):
        print("Flying")

class Penguin(BirdSwin):
    def swin(self):
        print("Swimming")
