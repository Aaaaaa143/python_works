# ==  =>checks the value 
# "is" => checks the identity or location

# if same variable stores same value then their locations are same 

# to find location => "id()"

a=10
b=10

print(a==b)

print(a is b)

print(id(a))
print(id(b))

c=a 
print(id(c))
