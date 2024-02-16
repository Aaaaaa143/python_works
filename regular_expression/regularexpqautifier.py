from re import *
text="abaabcaabaaaa"
# pattern="a+"   atleast one "a"
# pattern="a*"   matches for any number of "a"
# pattern="a?"   optional
# pattern="a{2}"   minimum 2 number of "a"
pattern="a{2,3}"   #minimum 2 and max 3 number of "a"
matcher=finditer(pattern,text)  #finditer() returns an itered variables

for m in matcher:
    print(m.start(),m.group())
