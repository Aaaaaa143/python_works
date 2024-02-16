cakes=[
    {"id":1,"name":"blueberry","shape":"rectangle","varient":[
        {"weight":"0.5kg","price":350},
        {"weight":"1kg","price":700},

    ]},
    {"id":2,"name":"nutbutter","shape":"round","varient":[
        {"weight":"0.5kg","price":450},
        {"weight":"1kg","price":900},

    ]},
    {"id":3,"name":"chocolate fudge","shape":"rectangle","varient":[
        {"weight":"0.5kg","price":550},
        {"weight":"1kg","price":1000},

    ]},
     {"id":4,"name":"cheesecake","shape":"round","varient":[
        {"weight":"0.5kg","price":650},
        {"weight":"1kg","price":1300},

    ]},
]


# 7qns
# all cake names

print([ca.get("name") for ca in cakes])

# cake with lowest price

price=min(v.get("price") for ca in cakes for v in ca.get("varient"))
print([ca.get("name") for ca in cakes for v in ca.get("varient") if v.get("price")==price])


# cost of  all 0.5kg cakes

print([v.get("price") for ca in cakes for v in ca.get("varient") if v.get("weight")=="0.5kg"])


# cost of all 1kg cakes

print([v.get("price") for ca in cakes for v in ca.get("varient") if v.get("weight")=="1kg"])


# name of round cakes
print([ca.get("name") for ca in cakes if ca.get("shape")=="round"])

# price of cheesecake 

print([v.get("price")  for ca in cakes for v in ca.get("varient") if  ca.get("name")=="cheesecake"])


# print name of all 1 kg cake ,price<800

print([ca.get("name") for ca in cakes for v in ca.get("varient") if( v.get("weight")=="1kg" )and( v.get("price")<800)])

