# valid usa mobile number
from re import*
text=input("enter the mobile number")
# pattern="[0-9]{3}[-]?[0-9]{3}[-]?[0-9]{4}"
pattern="[0-9]{3}[-\s]?[0-9]{3}[-\s]?[0-9]{4}"  #or "\d{3}[-]\d{3}[-]\d{4}"  \s means=> space
matcher=fullmatch(pattern,text)
print("invalid" if matcher==None else"valid")