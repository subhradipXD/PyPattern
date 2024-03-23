# output:
# enter row: 5
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

row = int(input("enter row: "))
for i in range(row):
    for j in range(row):
        print("*", end="")
    print("")