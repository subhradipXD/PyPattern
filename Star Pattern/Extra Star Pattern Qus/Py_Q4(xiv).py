# Pattern xiv


row = int(input("Enter the number of rows: "))
n=(row-1)//2
for i in range(row):
    for j in range(row):
        if (i<=n and j>=n and i-j>=-n) or (i>=n and j<=n and i-j<=n): 
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()