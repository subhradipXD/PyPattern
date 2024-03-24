# enter the row: 4
# 6 6 6 6
# 5 5 5
# 4 4
# 3
row = int(input("enter the row: "))
num = 6
for i in range (row):
    for j in range(row-i):
        print(num, end=" ")
    num -= 1
    print()