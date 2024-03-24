# enter the row: 5
#      *
#     ***
#    *****
#   *******
#  *********

row = int(input("enter the row: "))
for i in range(row):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i+1):
        print("*", end="")
    print()