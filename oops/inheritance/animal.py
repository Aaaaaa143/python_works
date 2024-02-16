class animal:
    name:str
    def __init__(self,name):
        self.name=name
    
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print(f"{self.name} barks")

    def __str__(self):
        return self.name
    
class frog(animal):
    def sound(self):
        print(f"{self.name} croaks")

    def __str__(self):
        return self.name
    
dobj=dog("dog")
dobj.sound()
fobj=frog("frog")
fobj.sound()
print(dobj.__class__)
print(dobj.__class__)