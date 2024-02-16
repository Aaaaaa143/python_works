# rule for validation aadhar number 3126 3456 3667(with and without space)
from re import*
aadhar=input("enter your aadhar number")
pattern="\d{4}(\s)?\d{4}(\s)?\d{4}"

matcher=fullmatch(pattern,aadhar)
print("invalid" if matcher==None else "valid")