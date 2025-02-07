from __future__ import annotations
from pydantic import BaseModel


class User(BaseModel):
    name: str
    mediator: ChatMediator | None = None

    def receive(self, message: str):
        print(f"{self.name} recebeu a mensage: {message}")

    def sender(self, message: str, recipient: str):
        self.mediator.notify(message, recipient)


class ChatMediator(BaseModel):
    users: dict[str, User]

    def notify(self, message: str, recipient):
        self.users[recipient].receive(message)

    def broadcast(self, message: str):
        for _, user in self.users.items():
            user.receive(message)


user_01 = User(name="User 01")
user_02 = User(name="User 02")
user_03 = User(name="User 03")

manager_chat = ChatMediator(
    users={"user_01": user_01, "user_02": user_02, "user_03": user_03}
)

user_01.mediator = manager_chat
user_02.mediator = manager_chat
user_03.mediator = manager_chat


user_01.sender("Eai usário 02 como voce vai?", "user_02")
user_02.sender("Eai cara recebi sua mensagem", "user_01")
manager_chat.broadcast("Pessoal vão todos dormir!")
