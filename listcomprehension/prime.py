num=int(input("enter a number"))
prime=[num%i==0 for i in range(2,num)]
print("prime" if any(prime)==False else "not prime")