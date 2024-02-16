word="chicken"
count=len(word)
str=sorted(word)
for i in range(0,count):
    j=i+1
    if str[i]==str[j]:
        print(str[i])

    