x = int(input())
n = int(input())

available = 0
for i in range(n):
    usage = int(input())
    available = available + (x - usage)

available = available + x
print(available)