# kl vehicle KL-08-A 
from re import*
vehicle=input("enter your vehicle number")
pattern="(KL)[-\s]?\d{2}[-\s]?[A-Z]{1,2}[-\s]?\d{4}"

matcher=fullmatch(pattern,vehicle)
print("invalid" if matcher==None else "valid")