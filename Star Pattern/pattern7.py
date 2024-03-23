# enter the row: 5
#      *
#     * *
#    *   *
#   *     *
#  *********
row = int(input("enter the row: "))
for i in range(row):
    for j in range(row-i):
        # prints the left space in the same row 
        print(" ", end="")
    for j in range(2*i+1):
        # printing the left boundary
        if j==0 or j==2*i or i==row-1:
            print("*", end="")
        else:
            # print space in middle
            print(" ", end="")
    print()