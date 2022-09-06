n = int(input())
villages = []

for i in range(n):
    villages.append(int(input()))

villages.sort()

min = 1000000000000
for i in range(1, len(villages) - 1):
    size = (villages[i] - villages[i - 1]) / 2 + (villages[i + 1] - villages[i]) / 2
    if min > size:
        min = size

print(f"{min:.1f}")