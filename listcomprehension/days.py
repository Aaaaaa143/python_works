# print from 1to 7 and print holiday if 1or 7 else weekdays
lst=[i for i in range(1,8)]
# days=["holiday" if num==1 or num==7 else"weekday" for num in lst]
# or 
days=["holiday" if num in (1,7) else"weekday" for num in lst]

print(days)
