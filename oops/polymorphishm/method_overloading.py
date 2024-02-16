# function overloading
# same function name but  different number of parameters

class operation:
    def add(self,n1,n2):
        return n1+n2
    def add(self,n1,n2,n3):
        return n1+n2+n3
    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4
op=operation()
# op.add(1,2)   
# op.add(1,2,3)
print(op.add(2,3,4,5))   #only this  method works