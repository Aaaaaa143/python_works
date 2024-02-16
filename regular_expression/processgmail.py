from re import *
f=open("C:\\Users\\DHANUJA\\Desktop\\python_works\\regular_expression\\gmaildata.txt")
pattern="[a-z0-9_.]+@[a-z]{2,}.com"
for line in f:
    mail=line.rstrip("\n")
    matcher=fullmatch(pattern,mail)
    if matcher != None:
        print(mail)

