lst=[
    [1803,1805,1809],
    [1909,1911,1913],
    [2000,2004,2005],
    [2011,2012,2013]
]
for data in lst:
    
    for d in data:
        if(d%100==0 and d%400==0):
            print(data)
            break
        elif (d%100!=0 and d%4==0):
            print(data)
            break
        else:
            break
    