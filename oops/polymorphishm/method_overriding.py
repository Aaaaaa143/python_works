# function overriding
# same function name and same number of paramters  
# function in parent class is over rided by function in child class

class parent:

    def mobile(self):
        print("samsung")
    
    def car(slef):
        print("swift")

class child(parent):
    def mobile(self):
        print("iphone")

ch=child()
ch.mobile()
ch.car()