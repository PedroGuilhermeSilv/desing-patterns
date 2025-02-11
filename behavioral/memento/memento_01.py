from typing import Any, Union, Generic, TypeVar
from copy import deepcopy

T = TypeVar("T")


class Memento(Generic[T]):
    def __init__(self, state: T) -> None:
        self._state: T
        super().__setattr__("_state", state)

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError("I am Immutable")

    def __str__(self) -> str:
        return f"Memento: {self.__dict__}"


class Originator:
    def __init__(self, name: str) -> None:
        self._name = name

    def save_state(self) -> Memento:
        return Memento[Originator](deepcopy(self))

    def __str__(self) -> str:
        return f"Origiantor {self._name}"


class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._states: list[Memento] = []
        self._originator: Union[Originator] = originator

    def backup(self) -> None:
        self._states.append(self._originator.save_state())

    def rollback(self) -> Memento:
        if self._states:
            self._states.pop()
            self._originator = self._states[-1]
            return self._originator
        return self._originator


originator = Originator("01")
manager = Caretaker(originator)
manager.backup()
print(manager._originator)

manager._originator._name = "02"
manager.backup()
print(manager._originator)
manager.rollback()
print(manager._originator)
