# f=open("txt path","mode")


f=open("C:\\Users\\DHANUJA\\Desktop\\python_works\\file_operation\\data.txt","r")

# for line in f:
#     print(line)
# print([line for line in f])    here the o/p is ['hello\n','hai\n','hello']
print([line.rstrip("\n") for line in f])
f.close()
