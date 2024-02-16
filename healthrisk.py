gender="male"
tummy_size=30
buttock_size=34
value=tummy_size/buttock_size
print(f"{value}")
if(gender=="male"):
    if(value<=0.95):
        print("health risk is low ")
    elif(value>0.95 and value<=1.0):
        print("health risk is moderate")
    else:
        print("health risk is high")
else:
    if(value<=.80):
        print("health risk is low ")
    elif(value>0.80 and value<=0.85):
        print("health risk is moderate")
    else:
        print("health risk is high")
    


