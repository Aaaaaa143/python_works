# list +ve number divisible by 3

lst=[2,3,4,6,-1,0,5,8]

num=[i for i in lst if (i>0 and i%3==0)]
print(num)
