from abc import ABC, abstractmethod

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Render Windows Checkbox"


class MacCheckbox(Checkbox):
    def paint(self):
        return "Render Mac Checkbox"