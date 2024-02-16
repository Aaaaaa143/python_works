num1=10
num2=20
num3=30
if(((num1>num2)and (num1<num3))or((num2>num1)and(num1>num3))):
    print(f"2nd largest={num1}")
elif(((num2>num1)and (num2<num3))or((num1>num2)and(num2>num3))):
     print(f"2nd largest={num2}")
elif(((num3>num1)and (num3<num2))or((num3>num2)and(num3<num1))):
     print(f"2nd largest={num3}")




# if(num1>num2)and(num1>num3):
#      if(num2>num3):
#           print(f"{num2}is 2nd largest")
#      else:
#           print(f"{num3} is 2nd largest")
# elif(num2>num1)and(num2>num3):
#      if(num1>num3):
#           print(f"{num1}is 2nd largest")
#      else:
#           print(f"{num3} is 2nd largest")
# elif(num3>num1)and(num3>num2):
#      if(num1>num2):
#           print(f"{num1}is 2nd largest")
#      else:
#           print(f"{num2} is 2nd largest")
