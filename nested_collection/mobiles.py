mobiles=[
    {"id":1,"name":"samsungs22","brand":"samsung","varients":[
        {"ram":"8gb","rom":"128gb","price":84000},
        {"ram":"8gb","rom":"256gb","price":100000},

    ]}, 
    {"id":2,"name":"samsungsa52","brand":"samsung","varients":[
        {"ram":"4gb","rom":"128gb","price":54000},
        {"ram":"8gb","rom":"256gb","price":65000},

    ]},
     {"id":3,"name":"one plus nord2","brand":"one plus","varients":[
        {"ram":"8gb","rom":"128gb","price":34000},
        {"ram":"8gb","rom":"256gb","price":45000},

    ]},
     {"id":4,"name":"miii1","brand":"redmi","varients":[
        {"ram":"8gb","rom":"128gb","price":24000},
        {"ram":"8gb","rom":"256gb","price":35000},

    ]},


]

# all mobile names

all_mobile_name=[mob.get("name") for mob in mobiles]
print(all_mobile_name)

# all brand names

brand_name=[mob.get("brand") for mob in mobiles]
print(set(brand_name))


# print mobile names in range 20k-30k

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("price") in range(20000,30001):
#             print(mob.get("name"))


price_filter=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("price") in range(20000,30001)]
print(price_filter)



# print name of mobiles with ram=4gb

# for mob in mobiles:
#     for v in mob.get("varients"):
#         if v.get("ram")=="4gb":
#             print(mob.get("name"))

ram_filter=[mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("ram")=="4gb"]
print(ram_filter)


# 8gb ram and price<40000


# for mob in mobiles:
#     for v in mob.get("varients"):
#          if (v.get("ram")=="8gb") and( v.get("price")<40000):
#              print(mob.get("name"))


print([mob.get("name") for mob in mobiles for v in mob.get("varients") if (v.get("ram")=="8gb") and (v.get("price")<40000)])


# costly mobile

price=max([v.get("price") for mob in mobiles for v in mob.get("varients")])
print(price)
print([mob.get("name") for mob in mobiles for v in mob.get("varients") if v.get("price")==price] )



