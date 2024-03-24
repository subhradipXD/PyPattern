# enter the row: 5
# 11111
# 22222
# 33333
# 44444
# 55555
row = int(input("enter the row: "))
num = 1
for i in range(row):
    for j in range(row):
        print(num, end="")
    num = num+1
    print()
