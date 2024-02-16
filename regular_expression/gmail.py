# gmailid validation
from re import *
gmail=input("enter the gamil id")
pattern="[a-z0-9_.]+(@gmail.com)"
matcher=fullmatch(pattern,gmail)
print("invalid" if matcher==None else "valid")