from dataclasses import dataclass
from abc import ABC, abstractmethod
import enum


class Method(enum.Enum):
    EMAIL = "Email"
    SMS = "SMS"


@dataclass
class Notify(ABC):
    destination: str
    message: str
    status: str

    @abstractmethod
    def send_message(self):
        pass


class SMS(Notify):
    def send_message(
        self,
    ):
        print(f"Enviando sms para {self.destination} | status: {self.status}")


class Email(Notify):
    def send_message(
        self,
    ):
        print(f"enviando email para {self.destination} | status: {self.status}")


@dataclass
class ChannelFactory(ABC):
    channels: dict[Method, Notify]

    def create_notify(self, method: Method) -> Notify:
        return self.channels.get(method)


class ChannelA1(ChannelFactory): ...


class ChannelA2(ChannelFactory): ...


if __name__ == "__main__":
    channel_factory = ChannelA1(channels={Method.EMAIL: Email})
    notify = channel_factory.create_notify(method=Method.EMAIL)
    notify: Notify = notify("destino", "messagem", "pendente")
    notify.send_message()

    channel_factory = ChannelA2(channels={Method.SMS: SMS})
    notify = channel_factory.create_notify(method=Method.SMS)
    notify("destino", "messagem", "pendente").send_message()
