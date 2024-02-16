num=321
sum=0
while(num!=0):
    last_digit=num%10
    sum=sum+last_digit
    num=num//10
print(sum)