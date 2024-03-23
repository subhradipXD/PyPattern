# output:
# enter row: 5
# *****
#  *****
#   *****
#    *****
#     *****
row = int(input("enter row: "))
for i in range(0, row):
    for j in range(1, i + 1):
        print(" ", end="")
    for k in range(0, row):
        print("*", end="")
    print()
