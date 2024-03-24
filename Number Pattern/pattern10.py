# enter the row: 5
# 1  
# 0 1  
# 0 1 0  
# 1 0 1 0  
# 1 0 1 0 1 
row = int(input("enter the row: "))
num = 1
for i in range (row):
    for j in range(i+1):
        print(num, end=" ")
        if num == 1:
            num = 0
        else:
            num = 1
    print(" ")