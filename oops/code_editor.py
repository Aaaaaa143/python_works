class editor:
    name:str

    def __init__(self,name):
        self.name=name

    def spec(self):
        pass

class vscode(editor):
    def spec(self):
        print(f"{self.name} supports edit,run,extension support,debugg")

    def __str__(self):
        return self.name
    
class pycharm(editor):
    def spec(self):
        print(f"{self.name} supports edit,run,debugg")
    
    def __str__(self):
        return  self.name
    
vobj=vscode("vscode")
vobj.spec()
print(vobj)

pobj=pycharm("pycharm")
pobj.spec()
print(pobj)
    

