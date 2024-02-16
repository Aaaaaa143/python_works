from json import load
path="C:\\Users\\DHANUJA\\Desktop\\python_works\\countries\\data.json"
with open(path,encoding="utf-8") as f:
    data=load(f)

print(len(data))

# print all regions

print({r.get("region") for r in data})

# asian countries

asian=[c.get("name") for c in data if c.get("region")=="Asia"]
print(asian)

# independent countries

print([c.get("name") for c in data if c.get("independent")==True])

# name of country with highest population

population=max(data,key=lambda m:m.get("population"))
print(population.get("name"))

# countries that share border with india

print([c.get("borders") for c in data if c.get("name")=="India"])