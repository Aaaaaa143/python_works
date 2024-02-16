for row in range(1,7):
    for space in range(6,row,-1):
        print(end="  ")
    for col in range(1,row+1):
        print("*  ",end=" ")
        
    print()