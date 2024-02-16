# logic2
num1=10
num2=20
print(f"before swapping num1={num1},num2={num2}")
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(f"after swapping num1={num1},num2={num2}")
# logic3
(num1,num2)=(num2,num1)
print(f"after swapping num1={num1},num2={num2}")
