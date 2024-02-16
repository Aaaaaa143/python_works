# starting with an alhpabet k,l,m,n 
# second must be a digit and divisible by 3
# followed by any number of alphabet and digits

from re import*
text=input("enter a text")
pattern="[k-n][369][a-zA-Z0-9]*"  #[\w] means =>[a-zA-Z0-9]
matcher=fullmatch(pattern,text)
if matcher==None:
    print("invalid")
else:
    print("valid")