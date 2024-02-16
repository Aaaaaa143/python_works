# self represent current class
# super represent parent class

class parent:
    def vehicle(self):
        self.context=["passionpro","swift"]
        return self.context
    
class child(parent):
    def vehicle(self):
        self.context=super().vehicle()
        self.context.append("ola")
        return self.context
p=parent()
print(p.vehicle())
c=child()
print(c.vehicle())