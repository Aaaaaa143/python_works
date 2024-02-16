class book:
    name:str
    author:str
    publisher:str

    def __init__(self,name,author,publisher):
        self.name=name
        self.author=author
        self.publisher=publisher
    
    def display(self):
        print(self.name,self.author,self.publisher)

    def __str__(self):
        return self.name
    
obj=book("i too had a love story","ravidar singh","blaa")
print(obj)