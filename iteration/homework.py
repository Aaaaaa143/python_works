num=int(input("enter the number"))
sum=0
i=1
out=0
while(i<=num):
    sum=num+sum*10
    out=out+sum
    i+=1
    print(sum)
print(out)