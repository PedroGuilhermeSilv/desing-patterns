from typing import Any
from dataclasses import dataclass


class GameSettings:
    _instance = {}

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls)
        return cls._instance[cls]


@dataclass
class InitConfig(GameSettings):
    def __init__(self, platform: str):
        self.platform = platform

    def __str__(self) -> str:
        return f" Settings: {self.platform}"


@dataclass
class Game01:
    config: GameSettings
    name: str


@dataclass
class Game02:
    config: GameSettings
    name: str


config = InitConfig(platform="xbox")


game01 = Game01(config, "Soccer")
print(f" Config: {game01.config} game:{game01.name}")
game02 = Game02(config, "Voleybol")
print(f" Config: {game02.config} game:{game02.name}")


config.platform = "playstation"
print(f" Config: {game01.config} game:{game01.name}")
print(f" Config: {game02.config} game:{game02.name}")
