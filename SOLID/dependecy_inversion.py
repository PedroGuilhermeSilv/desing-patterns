# Má implementação - Violando DIP
class MySQLDatabase:
    def save(self, data):
        print(f"Salvando dados {data} no MySQL")


class MongoDatabase:
    def save(self, data):
        print(f"Salvando dados {data} no MongoDB")


class UserService:
    def __init__(self):
        # Dependência direta de uma implementação concreta
        self.database = MySQLDatabase()

    def save_user(self, user_data):
        # Fortemente acoplado ao MySQL
        self.database.save(user_data)


# Boa implementação - Seguindo DIP
from abc import ABC, abstractmethod
from typing import Protocol


# Definindo a abstração (pode ser Interface/Protocol ou classe abstrata)
class Database(ABC):
    @abstractmethod
    def save(self, data: dict) -> None: ...
    @abstractmethod
    def delete(self, id: str) -> None: ...
    @abstractmethod
    def update(self, id: str, data: dict) -> None: ...
    @abstractmethod
    def get(self, id: str) -> dict: ...


# Implementações concretas
class MySQLDatabase(Database):
    def save(self, data: dict) -> None:
        print(f"Salvando {data} no MySQL")

    def delete(self, id: str) -> None:
        print(f"Deletando registro {id} do MySQL")

    def update(self, id: str, data: dict) -> None:
        print(f"Atualizando registro {id} com {data} no MySQL")

    def get(self, id: str) -> dict:
        print(f"Buscando registro {id} no MySQL")
        return {"id": id, "data": "mysql_data"}


class MongoDatabase(Database):
    def save(self, data: dict) -> None:
        print(f"Salvando {data} no MongoDB")

    def delete(self, id: str) -> None:
        print(f"Deletando registro {id} do MongoDB")

    def update(self, id: str, data: dict) -> None:
        print(f"Atualizando registro {id} com {data} no MongoDB")

    def get(self, id: str) -> dict:
        print(f"Buscando registro {id} no MongoDB")
        return {"id": id, "data": "mongo_data"}


# Serviço de alto nível dependendo de abstração
class UserService:
    def __init__(self, database: Database):
        # Depende da abstração, não da implementação
        self.database = database

    def create_user(self, user_data: dict) -> None:
        self.database.save(user_data)

    def delete_user(self, user_id: str) -> None:
        self.database.delete(user_id)

    def update_user(self, user_id: str, user_data: dict) -> None:
        self.database.update(user_id, user_data)

    def get_user(self, user_id: str) -> dict:
        return self.database.get(user_id)
