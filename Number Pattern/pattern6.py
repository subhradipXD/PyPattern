# enter the row: 4
# 3
# 4 4
# 5 5 5
# 6 6 6 6
row = int(input("enter the row: "))
num = 3
for i in range(row):
    for j in range(i+1):
        print(num, end=" ")
    num += 1
    print()