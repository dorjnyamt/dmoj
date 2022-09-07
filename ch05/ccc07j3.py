AMOUNTS = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
# NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

opened = int(input())
for case in range(opened):
    briefcase = int(input())
    AMOUNTS[briefcase - 1] = 0

average = sum(AMOUNTS) / (10 - opened)
offer = int(input())

if offer > average:
    print("deal")
else:
    print("no deal")