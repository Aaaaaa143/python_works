mobile={"name":"redmi","color":"black","price":15000,"ram":"8gb"}
if "price" in mobile:
    print(mobile["price"])
else:
    print("invalid key")

mobile["offer"]=1000
mobile["price"]-=1000
print(mobile)
