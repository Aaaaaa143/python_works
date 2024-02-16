f_read=open("C:\\Users\\DHANUJA\\Desktop\\python_works\\file_operation\\vehicle_number.txt")
f_write=open("C:\\Users\\DHANUJA\\Desktop\\python_works\\file_operation\\kerala_num.txt","w")

for line in f_read:
    reg=line.strip("\n")
    if reg.startswith("kl"):
        f_write.write(reg+"\n")

