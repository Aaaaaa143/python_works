# objects are stored in dictionary as key and Value

# value is acessed using Key

# dict_name={"key":"value","key":"value",...} 

student={"id":33,"name":"dhanuja","course":"python","age":22}
print(student["name"],student["course"])


# in =>checks whether the key is present or not 

print(" present" if "name" in student else " not present")

# or

# if "name" in student:
#     print("present")
# else:
#     print("not present")

#adding a value to dictionary eg:
student["mark"]=56
print(student)

#to update the value of dictionary eg:
student["mark"]+=20
print(student["mark"])



