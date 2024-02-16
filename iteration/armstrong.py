num=input("enter the number")
digit_count=len(num)
num=int(num)
original=num
sum=0
while(num!=0):
    last_digit=num%10
    power=last_digit**digit_count
    sum+=power
    num=num//10
print(sum)
print("armstrong number" if sum==original else "not armstrong number") 