from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsButton(Button):
    def paint(self):
        return "Render Windows Button"


class MacButton(Button):
    def paint(self):
        return "Render Mac Button"