num1=int(input("enter the number1"))
num2=int(input("enter the number2"))
hcf=1
smallest_num=num1 if num1<num2 else num2
for i in range(1,smallest_num+1):
    if num1%i==0 and num2%i==0:
        hcf=i
print(f"HCF={hcf}")