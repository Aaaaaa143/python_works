class book:
    data=[
        {"id":100,"name":"python","price":350},
        {"id":101,"name":"java","price":450},
        {"id":102,"name":"django","price":1300},
        {"id":103,"name":"html","price":1000},
        {"id":104,"name":"bootstrap","price":300},
    ]

    def get(self,*args,**kwargs):
        return self.data
    
    def retrive(self,id,*args,**Kwargs):
        obj=[b for b in self.data if b.get("id")==id].pop()
        return obj
    
    def put(self,id,*args,**kwargs):
        obj=[b for b in self.data if b.get("id")==id].pop()
        obj.update(kwargs)
        return f"{obj} has been updated !!!"
    
    def distroy(self,id,*args,**kwargs):
        obj=[b for b in self.data if b.get("id")==id].pop()
        self.data.remove(obj)
        return f"{obj} removed!!"


obj=book()
print(obj.get())
print(obj.retrive(103))
print(obj.put(102,price=1500))
print(obj.distroy(104))