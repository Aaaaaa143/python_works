data=[
        {"id":100,"name":"galaxya5","price":35000},
        {"id":101,"name":"mi11i","price":25000},
        {"id":102,"name":"iphone15","price":135000},
        {"id":103,"name":"s23","price":145000},
        {"id":104,"name":"neo","price":35000},
        

    ]
def create(*args,**kwargs):
    data.append(kwargs)
    return f"{kwargs} created successfully"

print(create(id="101",name="iphone12",price=70000))

def retrive(id=None):
    for d in data:
        if id==d.get("id"):
            return d
        
print(retrive(id=103))


#list all data



#delete
def distroy(*args,**kwargs):
    id=kwargs.get("id")
    obj=[mob for mob in data if mob.get("id")==id].pop()
    data.remove(obj)
    return f"{obj} is removed"

print(distroy(id=100))


#update

def put(id,*args,**kwargs):
    obj=[mob for mob in data if mob.get("id")==id].pop()
    obj.update(kwargs)
    return f"{obj} has been updated"

print(put(id=104,name="redmi",price=30000))