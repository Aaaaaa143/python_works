lst=[10,11,12,13,14,15]
num=12
for i in range(0,len(lst)):
    if  num==lst[i]:
        print("element found")
        break
else:
    print("element not found")
