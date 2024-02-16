
f=open("C:\\Users\\DHANUJA\\Desktop\\python_works\\file_operation\\data.txt","r")

# f.write("hello good morning"+"\n")

# lst=["hai","hello","hai","hloo"]

# for w in lst:
#     f.write(w+"\n")


f1=open("C:\\Users\\DHANUJA\\Desktop\\python_works\\file_operation\\years.txt","w")
for line in f:
    year=int(line.strip("\n"))
    if year%100==0 and year%400==0:
        f1.write(str(year)+"\n")
    elif year%100!=0 and year%4==0:
        f1.write(str(year)+"\n")

    



f.close()





    # write leap yr to year.txt

