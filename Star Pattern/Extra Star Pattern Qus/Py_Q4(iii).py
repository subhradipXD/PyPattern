# Pattern iii


row = int(input("Enter the number of rows: "))
for i in range(row):
    for j in range(row):
        if i<=j:
            print("*", end=" ")
    print()