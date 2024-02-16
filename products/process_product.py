from json import load

path="C:\\Users\\DHANUJA\\Desktop\\python_works\\products\\items.json"
with open(path,encoding="UTF-8")as f:
    data=load(f)

# print total  number of products
print(len(data))


# print all catagories

print({ c.get("category")for c in data})


# print electronic product names 

print([c.get("title") for c in data if c.get("category")=="electronics"])

# top rated products

top_rated=max(data,key=lambda m:m.get("rating").get("rate"))
print(top_rated.get("title"))


# product having category womens clothing price range(100-300)

print([c.get("title") for c in data if (c.get("category")=="women's clothing" and c.get("price")>20 and c.get("price")<50 )])

# which product has the most rating count

most_rating=max(data,key=lambda m:m.get("rating").get("count"))
print(most_rating.get("title"))


# jewlery rating >3

print([c.get("title") for c in data  if (c.get("category")=="jewelery" and c.get("rating").get("rate")>3)])



# sort products wrt price
srt=sorted(data,reverse=True,key=lambda m:m.get("price") )
for p in srt:
    print(p.get("title"))

# categorywise product count
wc={}
for c in data:
    category=c.get("category")
    if category not in wc:
        wc[category]=1
    else:
        wc[category]+=1
print(wc)

# print product category with max count
val_key=[(v,k) for k,v in wc.items()]
print(max((val_key)))
