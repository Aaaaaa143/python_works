# print 1800to2024

year=[yr for yr in range(1800,2025)]
print(year)

# print century year 
century_year=[yr for yr in range(1800,2025) if yr%100==0]
print(century_year)

# print leap year
leap_year=[yr for yr in year if(yr%100==0 and yr%400==0)or(yr%100!=0 and yr%4==0 )]
print(leap_year)
