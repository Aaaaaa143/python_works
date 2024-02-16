num1=int(input("enter the number1:> "))
num2=int(input("enter the number2:> "))
lg_num= num1 if num1>num2 else num2

#with equation

# sm_num=num1 if num1<num2 else num2
# gcd=1
# for i in range(1,sm_num+1):
#     if num1%i==0 and num2%i==0:
#         gcd=i
# lcm=(num1*num2)/gcd
# print(f"lcm={lcm}")


# without equation

lcm=1
product=num1*num2
for i in range(lg_num,product+1):
    if i%num1==0 and i%num2==0:
        lcm=i
        break
        
print(f"lcm={lcm}")
