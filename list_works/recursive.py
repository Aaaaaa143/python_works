# print the 1st recursive character

text="ABACCD"

lst=[]
dup_lst=[]
for ch in text:
    if lst.count(ch)==0:
        lst.append(ch)
    else:
       print(f"1st recursive={ch}")
       break


    
# to print the 2nd recursive


#     else:
#         dup_lst.append(ch)

# print(dup_lst[1])
    
    
    
