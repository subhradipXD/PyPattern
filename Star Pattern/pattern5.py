# enter the row: 5
# *
# **
# ***
# ****
# *****
row = int(input("enter the row: "))
for i in range(row):
    for j in range (0, i+1):
        print("*", end="")
    print()