frameworks=[
    {"id":1,"name":"django","rating":5,"language":"python"},
    {"id":2,"name":"angular","rating":4,"language":"typescript"},
    {"id":3,"name":"react","rating":5,"language":"javascript"},
    {"id":4,"name":"spring","rating":3,"language":"java"},
    {"id":5,"name":"asp.net","rating":2,"language":"c#"},
    {"id":6,"name":"flask","rating":3,"language":"python"},
]

# for fw in frameworks:
#     print(fw.get("name"))


fw_name=[fw.get("name") for fw in frameworks]
print(fw_name)


# for fw in frameworks:
#     print(fw.get("rating"))

all_rating=[fw.get("rating") for fw in frameworks]
print(all_rating)

# name of language=python

# for fw in frameworks:
    # if fw.get("language")=="python":
        # print(fw.get("name"))

python=[fw.get("name") for fw in frameworks if fw["language"]=="python"]
print(python)

# name of rating =5
rating=[fw.get("name") for fw in frameworks if fw.get("rating")==5]
print(rating)

# id from 1 to 3

id_filter=[fw.get("name") for fw in frameworks if fw.get("id") in range(1,4)]
print(id_filter)


# print the minimum  rating dictionary

lowest_rating=min(frameworks,key=lambda fw:fw.get("rating"))
print(lowest_rating)

#  print the minimum  rating dictionary

highest_rating=max(frameworks,key=lambda fw:fw.get("rating"))
print(highest_rating)

# sorted rating in decreasing order

sorted_rating=sorted(frameworks,reverse=True,key=lambda fw:fw.get("rating"))
print(sorted_rating)

