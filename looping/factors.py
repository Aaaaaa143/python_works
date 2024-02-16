
# print common factors  of 12 and 24
num1=12
num2=24
for i in range(2,num1+1):
    if num1%i==0 and num2%i==0:
        print(i)
