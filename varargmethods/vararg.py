# * allows  to pass any number of parameters through a function
# eg:>

# def add(*n1):
#     print(n1)

# add(10,20,30)
# add(30,48)


def product(*args):
    res=1
    for n in args:
        res=res*n
    return res
print(product(10,20))
print(product(1,2,3,4,5,6))


def adder(*args):
    # res=0
    # for n in args:
    #     res=res+n
    # return res

    return sum(args)

print(adder(20,30,40))

number=input("enter the numbers").split(",")
print(number)