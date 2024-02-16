
# flag=False
# num=int(input("enter the number"))
# for i in range(2,num):
#     if num%i==0:
#         flag=True
#         break
# if flag==False:
#     print("prime number")
# else:
#     print("not prime number")


is_prime=True
num=int(input("enter the number"))
for i in range(2,num):
    if num%i==0:
        is_prime=False
        break
print(is_prime)