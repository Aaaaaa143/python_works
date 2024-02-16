from  json import load

# f=open("C:\\Users\\DHANUJA\\Desktop\\python_works\\process_jason\\students.json","r")

# data=load(f)

# # print(data)

# print(len(data))

# print([st.get("name") for st in data])

# f.close()

# or   


path="C:\\Users\\DHANUJA\\Desktop\\python_works\\process_jason\\students.json"
with open(path) as f:
    data=load(f)

print(data)