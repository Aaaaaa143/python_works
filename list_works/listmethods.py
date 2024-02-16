# "append(data)"  => to add new data to the list                                                                                                                                                      

colors=["red","green","blue","red"]
colors.append("yellow")
print(colors)


# count(data)  =>  to count the  number of times a data is present

print(colors.count("red"))


# "index(data)" => returns the location of the data in the list

print(colors.index("green"))


# " inset(index,data)"  =>  to insert data to a  particular position  in list

colors.insert(3,"black")
print(colors)


# " sort()"=> to sort the list in albhabetic order


colors.sort()
print(colors)



# "remove(data)" => to remove the 1st occurence of data from the list 

colors.remove("red")
print(colors)


# " pop(index)" => to delete the data in the specified index  by deafualt index=-1 {means last data in the list}

colors.pop(2)
print(colors)


# copy()  =>  to copy the data of the list to anathor variable


cpy_colors=colors.copy()
print(cpy_colors)

print(cpy_colors==colors)   #compares the value
print(cpy_colors is colors)  #compares the identity










