weight_kg=58
height_cm=163
height_m=height_cm/100
bmi=weight_kg/(height_m**2)
print(f"bmi={bmi}")
if(bmi<=19):
    print("underweight")
elif(bmi>19 and bmi<25 ):
    print("normal")
elif(bmi>24 and bmi<29):
    print("over weight")
elif(bmi>30):
    print("obesity")