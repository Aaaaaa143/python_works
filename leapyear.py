year=2100
# if century year then divisible by 400 and not century year divisible by 4
if(year%100==0 and year%400==0):
    print(f"{year} is a leap year")
elif(year%100!=0 and year%4==0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")