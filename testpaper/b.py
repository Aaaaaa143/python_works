text="ABABC"
wc=[]
dc=[]
for w in text:
    if wc.count(w)==0:
        wc.append(w)

    else:
        dc.append(w)
non_recursive=set(wc).difference(set(dc))
print(non_recursive)
