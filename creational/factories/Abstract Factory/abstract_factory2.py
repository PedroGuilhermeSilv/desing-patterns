from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum


@dataclass
class Platform(ABC):
    button: str = ""
    text: str = ""
    window: str = ""
    menu: str = ""

    @abstractmethod
    def show_button(self): ...
    @abstractmethod
    def show_text(self): ...
    @abstractmethod
    def show_window(self): ...
    @abstractmethod
    def show_menu(self): ...


@dataclass
class Windows(Platform):
    def show_button(self):
        return print("button windows")

    def show_menu(self):
        return print("menu windows")

    def show_text(self):
        return print(f"text windows {self.text}")

    def show_window(self):
        return print("window windows")


@dataclass
class MacOS(Platform):
    def show_button(self):
        return print("button MacOS")

    def show_menu(self):
        return print("menu MacOS")

    def show_text(self):
        return print(f"text MacOS {self.text}")

    def show_window(self):
        return print("window MacOS")


@dataclass
class Linux(Platform):
    def show_button(self):
        return print("button Linux")

    def show_menu(self):
        return print("menu Linux")

    def show_text(self):
        return print(f"text linux {self.text}")

    def show_window(self):
        return print("window Linux")


class PlatformFactory(ABC):
    @abstractmethod
    def get_windows(self) -> Windows: ...
    @abstractmethod
    def get_mac_os(self) -> MacOS: ...
    @abstractmethod
    def get_linux(self) -> Linux: ...


class InstagramFactory(PlatformFactory):
    def get_windows(self) -> Windows:
        return Windows(text="instagram")

    def get_mac_os(self) -> MacOS:
        return MacOS(text="Instagram")

    def get_linux(self) -> Linux:
        return Linux(text="instagram")


class TwitterFactory(PlatformFactory):
    def get_windows(self) -> Windows:
        return Windows(text="Twitter")

    def get_mac_os(self) -> MacOS:
        return MacOS(text="Twitter")

    def get_linux(self) -> Linux:
        return Linux(text="Twitter")


class NotebookWindows:
    @staticmethod
    def get_platforms():
        platforms: list[PlatformFactory] = [TwitterFactory(), InstagramFactory()]
        for platform in platforms:
            platform.get_windows().show_text()


class NotebookLinux:
    @staticmethod
    def get_platforms():
        platforms: list[PlatformFactory] = [TwitterFactory(), InstagramFactory()]
        for platform in platforms:
            platform.get_linux().show_text()


class NotebookMacOS:
    @staticmethod
    def get_platforms():
        platforms: list[PlatformFactory] = [TwitterFactory(), InstagramFactory()]
        for platform in platforms:
            platform.get_mac_os().show_text()


if __name__ == "__main__":
    notebook_windows = NotebookWindows.get_platforms()
    notebook_linux = NotebookLinux.get_platforms()
    notebook_macos = NotebookMacOS.get_platforms()
