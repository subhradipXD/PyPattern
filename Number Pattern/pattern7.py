# enter the row: 7
# 3
# 4 4
# 5 5 5
# 6 6 6 6
# 5 5 5
# 4 4
# 3
row = int(input("enter the row: "))
down = int(row/2)
up = row-down
num = 3
for i in range (up):
    for j in range(up):
        if i>=j:
            print(num, end=" ")
    num += 1
    print()
num -= 2
for i in range (down):
    for j in range(down - i):
        print(num, end=" ")
    num -= 1
    print()
