# read start and limit from user
i=int(input("enter number:>"))
limit=int(input("enter the limit:>"))
while(i<=limit):
    if i%2==0:
        print(i)
    i+=1