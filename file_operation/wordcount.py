f=open("C:\\Users\\DHANUJA\\Desktop\\python_works\\file_operation\\news.txt","r")

wc={}

for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        if w not in wc:
            wc[w]=1
        else:
            wc[w]+=1


print(wc)