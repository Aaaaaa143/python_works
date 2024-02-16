class superhero:

    def __init__(self,name):
        self.name=name

    def super_powers(self):
        self.context=["run","jump"]
        return self.context
    
class spiderman(superhero):

    def super_powers(self):
        self.context=super().super_powers()
        self.context.append("fly")
        self.context.append("webbing")
        return self.context
    
class minnal_murali(superhero):
    
    def super_powers(self):
        self.context=super().super_powers()
        self.context.append("speed")
        return self.context
    
obj=spiderman("spiderman")
print(obj.super_powers())
obj1=minnal_murali("minnal murali")
print(obj1.super_powers())