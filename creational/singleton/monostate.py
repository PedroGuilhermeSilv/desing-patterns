


class Monostate:
    # Estado compartilhado entre todas as instâncias
    _shared_state: dict = {"volume": 50, "brightness": 70, "language": "pt-br"}

    def __init__(self):
        # Faz com que todas as instâncias compartilhem o mesmo dicionário de estado
        self.__dict__ = self._shared_state


class GameConfig(Monostate):
    def update_volume(self, volume: int) -> None:
        self.volume = volume

    def update_brightness(self, brightness: int) -> None:
        self.brightness = brightness

    def update_language(self, language: str) -> None:
        self.language = language

    def __str__(self) -> str:
        return f"Config: [Volume: {self.volume}, Brightness: {self.brightness}, Language: {self.language}]"


if __name__ == "__main__":
    # Criando duas instâncias diferentes
    config1 = GameConfig()
    config2 = GameConfig()

    print("Estado inicial:")
    print(f"Config1: {config1}")
    print(f"Config2: {config2}")

    # Modificando config1
    config1.update_volume(75)
    config1.update_language("en-us")

    print("\nApós modificar config1:")
    print(f"Config1: {config1}")
    print(f"Config2: {config2}")  # Note que config2 também foi alterado

    # Modificando config2
    config2.update_brightness(90)

    print("\nApós modificar config2:")
    print(f"Config1: {config1}")  # Note que config1 também foi alterado
    print(f"Config2: {config2}")

    # Provando que são instâncias diferentes
    print("\nSão a mesma instância?")
    print(f"config1 is config2: {config1 is config2}")  # Retornará False
