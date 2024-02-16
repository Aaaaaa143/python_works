# constructor 

# used to initialise instance variable

# __init__()  => constructor in python

# constructor is called when object is created 

class student:
    rollnum:int
    course:str
    total:int
    def __init__(self,rollnum,course,total):
        self.roll=rollnum
        self.course=course
        self.total=total
    def display(self):
        print(self.roll,self.course,self.total) 
obj1=student(1000,"django",500)     # constructor is called.
obj1.display()
