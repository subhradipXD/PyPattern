row = int(input("enter the row: "))
for i in range(row):
    for j in range(row-i):
        print(" ",end="")
    for k in range(1, 2*i):
        print("*", end="")
    print()
for i in range (row-2, 0, -1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print()