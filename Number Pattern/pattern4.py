# enter the row: 5
# 15 14 13 12 11 
# 10 9 8 7 
# 6 5 4 
# 3 2 
# 1 
row = int(input("enter the row: "))
num = row * (row+1) // 2
for i in range(row):
    for j in range(row):
        if i <= j or i == 0:
            print(num, end=" ")
            num -= 1
    print()