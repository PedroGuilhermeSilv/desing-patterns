from __future__ import annotations
from abc import ABC, abstractmethod


# Interface comum para todos os estados
class EstadoMaquinaCafe(ABC):
    def __init__(self, maquina: MaquinaCafe) -> None:
        self.maquina = maquina

    @abstractmethod
    def preparar_cafe(self):
        pass

    @abstractmethod
    def reabastecer_agua(self):
        pass

    @abstractmethod
    def reabastecer_graos(self):
        pass


# Estados concretos
class EstadoPronto(EstadoMaquinaCafe):
    def preparar_cafe(self):
        if self.maquina.agua > 0 and self.maquina.graos > 0:
            print("Preparando café...")
            maquina.agua -= 1
            maquina.graos -= 1
            maquina.estado = EstadoPreparando(self.maquina)
        else:
            if maquina.agua == 0:
                maquina.estado = EstadoSemAgua(self.maquina)
            if maquina.graos == 0:
                maquina.estado = EstadoSemGraos(self.maquina)

    def reabastecer_agua(self):
        print("Água já está cheia.")

    def reabastecer_graos(self):
        print("Grãos já estão cheios.")


class EstadoPreparando(EstadoMaquinaCafe):
    def preparar_cafe(self):
        print("Café já está sendo preparado.")

    def reabastecer_agua(self):
        print("Não é possível reabastecer água enquanto prepara café.")

    def reabastecer_graos(self):
        print("Não é possível reabastecer grãos enquanto prepara café.")


class EstadoSemAgua(EstadoMaquinaCafe):
    def preparar_cafe(self):
        print("Não é possível preparar café. Sem água.")

    def reabastecer_agua(self):
        print("Reabastecendo água...")
        self.maquina.agua = 5
        self.maquina.estado = EstadoPronto(self.maquina)

    def reabastecer_graos(self):
        print("Grãos já estão cheios.")


class EstadoSemGraos(EstadoMaquinaCafe):
    def preparar_cafe(self):
        print("Não é possível preparar café. Sem grãos.")

    def reabastecer_agua(self):
        print("Água já está cheia.")

    def reabastecer_graos(self):
        print("Reabastecendo grãos...")
        self.maquina.graos = 5
        self.maquina.estado = EstadoPronto(self.maquina)


# Classe contexto que usa o estado
class MaquinaCafe:
    def __init__(self):
        self.estado = EstadoPronto(maquina=self)
        self.agua = 5
        self.graos = 5

    def preparar_cafe(self):
        self.estado.preparar_cafe()

    def reabastecer_agua(self):
        self.estado.reabastecer_agua()

    def reabastecer_graos(self):
        self.estado.reabastecer_graos()


# Exemplo de uso
maquina = MaquinaCafe()
maquina.preparar_cafe()  # Preparando café...
maquina.preparar_cafe()  # Café já está sendo preparado.
maquina.reabastecer_agua()  # Não é possível reabastecer água enquanto prepara café.
maquina.reabastecer_graos()  # Não é possível reabastecer grãos enquanto prepara café.
