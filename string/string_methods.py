name="LUMINaR TechnologY"
print(name.casefold())

# to convert entire string  to lower case we use the method casefold() 
#    syntax :>   object.casefold()
    # casefold can only be used on string


print(name.capitalize())

# capitalize() convert the 1st letter to upper case and others to lower case
#    syntax:>  object.capitalize()


print(name.count('a'))

# count() returns the count of the letter in the string
#     syntax:> object.count("character")
#  is case sensitive
#    to take count without  case sensitive use both "casfold" and "count" together


print(name.startswith("hu"))

#startswith() returns "true" if the string starts with the given string else "false"
#   syntax:> object.startswith("lu")   
#     o\p:> true
    #   startswith() is case sensitive

print(name.endswith("gY"))

# endswith() returns "true" or "false" corresponding to the string
#   syntax :> object.endswith("gy")

#endswith()is case sensitive

print(name.isalpha())
#isalpha() checks whether the string contains only alphabets or not and return either "true" or "false"

print(name.isdigit())
# isdigit() checks whether the string is digit or not and returns "true" or "false"


print(name.isalnum())
# isalnum()checks whether the string  contains only alphabets and digits and returns "true"or "false"

print(name.split(" "))
#split() it splits the words in the strings 

word=name.split(" ")
for w in word:
    print(w)

    #to print words of strings using  "for" to get words line by line

# strip() => to remove a character from string
# lstrip()=> to remove from left side
# rstrip()=> to remove from right side