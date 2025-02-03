
from abc import ABC, abstractmethod
from uuid import UUID, uuid4


class ICommand(ABC):
    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def undo(self,id: UUID): pass


class Cozinha(ABC):
    def __init__(self) -> None:
        self._pedidos: dict[UUID,str] ={}
    def fazer_pizza(self)-> str:
        self._pedidos[uuid4()]= "Pizza criada"
    
    def cancelar_pizza(self, id: UUID) ->None :
        self._pedidos.pop(id)

    def fazer_bebida(self)-> str:
        self._pedidos[uuid4()]= "bebida criada"
    
    def cancelar_bebida(self, id: UUID) ->None :
        self._pedidos.pop(id)


class PizzaCommand(ICommand):
    def __init__(self, cozinha: Cozinha) -> None:
        self.cozinha = cozinha

    def execute(self):
        self.cozinha.fazer_pizza()

    def undo(self, id: UUID):
        self.cozinha.cancelar_pizza(id)


class BebidaCommand(ICommand):
    def __init__(self, cozinha: Cozinha) -> None:
        self.cozinha = cozinha

    def execute(self):
        self.cozinha.fazer_bebida()

    def undo(self, id: UUID):
        self.cozinha.cancelar_bebida(id)


class GerenciadorPedidos:
    def __init__(self) -> None:
        self._commands: dict[str, ICommand] ={}

    def add_command(self,recurso: str, command: ICommand):
        self._commands[recurso] = command

    def execute(self,recurso:str):
        self._commands[recurso].execute()
    
    def undo(self,recurso:str, id:UUID):
        self._commands[recurso].undo(id)



cozinha = Cozinha()
pizza_commands = PizzaCommand(cozinha)
bebida_commands = BebidaCommand(cozinha)

gerenciador = GerenciadorPedidos()
gerenciador.add_command("criar pizza", pizza_commands)
gerenciador.add_command("cancelar pizza",pizza_commands)
gerenciador.add_command("criar bebida", bebida_commands)
gerenciador.add_command("cancelar bebida",bebida_commands)
        
print("Criando pedidos....")
gerenciador.execute("criar pizza")
gerenciador.execute("criar bebida")
print(cozinha._pedidos)
print("Pedidos cancelados...")
gerenciador.undo("cancelar pizza",next(iter(cozinha._pedidos)))
gerenciador.undo("cancelar bebida",next(iter(cozinha._pedidos)))
print(cozinha._pedidos)





