from abc import ABC,abstractmethod
class editor(ABC):

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def save(self):
        pass

class vscode(editor):

    def edit(self):
        print("vscode edit method")

    def debug(self):
        print("vscode debugg method")

    def run(self):
        print("vscode run method")

    def save(self):
        print("vscode save method")

obj=vscode()
obj.debug()
obj.run()
