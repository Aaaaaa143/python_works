# rule for a validate mobile number

from re import*
mob=input("enter your mobile number")
pattern="(91)?[0-9]{10}"

matcher=fullmatch(pattern,mob)
print("invalid" if matcher==None else "valid")