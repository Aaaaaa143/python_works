class mobile:
    data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},
        

    ]
    
    #create a mobile
    def create(self,*args,**kwargs):
        self.data.append(kwargs)
        return f"{kwargs} created !!!"
    

    #detail of a specific mobile
    def retrieve(self,id,*args,**kwargs):
        obj=[mob for mob in self.data if mob.get("id")==id].pop()
        return obj
    

    #list of all mobiles
    def get(self,*args,**kwargs):
        return f"{self.data}"
    

    #update 
    def put(self,id,*args,**kwargs):
        obj=[mob for mob in self.data if mob.get("id")==id].pop()
        obj.update(kwargs)
        return f"{obj} updated!!!"
    
    #delete
    def distroy(self,id,*args,**kwargs):
        obj=[mob for mob in self.data if mob.get("id")==id].pop()
        self.data.remove(obj)
        return f"{obj} has been removed !!!"
    


obj=mobile()
print(obj.create(id=105,name="redmi",price=40000))
print(obj.retrieve(id=101))
print(obj.get())
print(obj.put(id=103,name="samsung s23",price=140000))
print(obj.distroy(id=100))