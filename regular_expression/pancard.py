# pan card number validation
from re import*
pan=input("enter the PAN number")
pattern="[A-Z]{3}[PCAFHT]+[A-Z]{1}\d{4}[A-Z]{1}"
matcher=fullmatch(pattern,pan)
print("invalid" if matcher==None else "valid")



