# enter the row: 5
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *
row = int(input("enter the row: "))
for i in range (row):
    for j in range(0, row-i-1):
        print(" ", end="")
    for j in range(0, i+1):
        print("*", end="")
    print()
for i in range (1, row):
    for j in range(0, i):
        print(" ", end="")
    for j in range(0, row-i):
        print("*", end="")
    print()