# defined using '{ ,}'
#     or
# set=set() {used if the set is empty }

# can store any type of  datatypes

# duplicate is not allowed
# insertion order is not preserved ie, indexing is not supported

# update is allowed

# methods

# add() => to add data to the set

color_set={"red","blue","black"}
color_set.add("yellow")
print(color_set)

# union() => cobines the data of 2 sets

st2={"red","yellow","purple"}
union_set=color_set.union(st2)
print(union_set)


#intersection() => to take the common in 2 sets

intersection_set=color_set.intersection(st2)
print(intersection_set)


# difference() => removes elemnts of set2 from set1
print(color_set.difference(st2))

# pop() => to remove some data from set but not specified
color_set.pop()
print(color_set)


# remove() => to rmove a specified data from the set 
# returns error if the data is not present in the set
color_set.remove("black")
print(color_set)


# discard() => to remove specified  data  from the set but does not return error if the data is not present

st2.discard("purple")
print(st2)



# issubset() => to check whether the set is subset of the other set

print(color_set.issubset(st2))


# issuperset() => checks whether the set is superset of the other

print(st2.issuperset(color_set))


