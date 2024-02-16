class books:

    data=[
        {"id":101,"name":"vishappu","author":"basheer"},
        {"id":102,"name":"oru desathinte kadha","author":"s k pottakadu"},
        {"id":103,"name":"5 point someone","author":"chetan bhagath"},
        {"id":104,"name":"ikigai","author":"francesc miralles"},
        {"id":105,"name":"harry potter","author":"j k rowling"},

    ]

    def create(self,*args,**kwargs):
        self.data.append(kwargs)
        return f"{kwargs} created !!!"
    
    def retrieve(self,id,*args,**kwargs):
        obj=[bo for bo in self.data if bo.get("id")==id].pop()
        return f"{obj}"
    
    def get(self,*args,**kwargs):
        return self.data
    

    def put(self,id,*args,**kwargs):
        obj=[bo for bo in self.data if bo.get("id")==id].pop()
        obj.update(kwargs)
        return f"{kwargs} updated !!!"
    
    def distroy(self,id,*args,**kwargs):
        obj=[bo for bo in self.data if bo.get("id")==id].pop()
        self.data.remove(obj)
        return f"{obj} removed !!!"


obj=books()
print(obj.create(id=106,name="the advantures of tom swayer",author="mark twain"))
print(obj.retrieve(id=105))
print(obj.get())
print(obj.put(id=103,name="half girlfriend"))
print(obj.distroy(id=102))