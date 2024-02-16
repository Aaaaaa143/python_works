def add(n1,n2):
    return n1+n2
 
def sub(n1,n2):
    return n1-n2
def product(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
def cube(n):
    return n**3


def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1

print(smart_sub(8,23))