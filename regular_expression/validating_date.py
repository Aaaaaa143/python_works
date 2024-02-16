# validation of date in format YYYY-MM-DD 

from re import *
date=input("enter the date")
pattern="\d{4}[-\s]?\d{2}[-\s]?\d{2}"
matcher=fullmatch(pattern,date)
print("invalid" if matcher==None else "valid")
