# Enter the number of rows: 5
#         *
#       * *
#     * * *
#       * *
#         *
row = int(input("Enter the number of rows: "))
for i in range(row):
    for j in range(row):
        if i<=j and i+j>=row-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()