# enter the row: 5
#     1
#    212
#   32123
#  4321234
# 543212345
row = int(input("enter the row: "))
for i in range(1, row+1):
    for j in range(row-i):
        print(end=" ")
    for j in range(i, 0, -1):
        print(j, end="")
    for k in range(2, i+1):
        print(k, end="")
    print()
