# Pattern xi


row = int(input("Enter the number of rows: "))
n=row//2
for i in range(2*n+1):
    for j in range(2*n+1):
        if (((i+j)>=n) and ((j-i)<=n) and ((i-j)<=n) and ((i+j)<=3*n)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()