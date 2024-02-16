from re import *
text=input("enter a variable name")
pattern="[a-zA-Z][a-zA-Z0-9_]*"
matcher=fullmatch(pattern,text)  #returns none if it is not a match to the pattern
if matcher==None:
    print("invalid")

else:
    print("valid")
