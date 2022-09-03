from os import stat
import statistics

n = int(input())
qr = []
a = list(range(1, n + 1))
for i in range(n):
    qr.append(input())

for i in range(1, n - 1):
    for j in range(n):
        if qr[i][j] == "1":
            # while (a[i] != j):
            if a[i] != j:
                print("NEED SWAP", a[i], j)
            b = a[i-1:i+2]
            # b.sort()
            print(b)
print(a)