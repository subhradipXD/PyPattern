# enter the row: 5
# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4  
# 1 2 3 4 5  
row = int(input("enter the row: "))
for i in range (row):
    for j in range(i+1):
        print(j+1, end=" ")
    print(" ")