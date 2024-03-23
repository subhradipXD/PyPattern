# enter row: 5
#       *****
#      *****
#     *****
#    *****
#   *****

row = int(input("enter row: "))
for i in range (0, row):
    for j in range (0, row-i+1):
        print(end=" ")
    for j in range (0, row):
        print("*", end="")
    print()