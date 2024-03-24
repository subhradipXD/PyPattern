# enter the row: 5
#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5
row = int(input("enter the row: "))
for i in range(1, row+1):
    for j in range(row-i):
        print(end=" ")
    for j in range(i):
        print(i, end=" ")
    print()