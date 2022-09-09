readings = int(input())
levels = list(map(int, input().split()))

lowest = min(levels)
highest = max(levels)
where_lowest = levels.index(lowest)
where_highest = levels.index(highest)

unknown = False
for level in range(where_lowest, where_highest - 1):
    prev = levels[level]
    next = levels[level + 1]
    if prev > next:
        unknown = True

if where_lowest > where_highest:
    unknown = True
if unknown:
    print("unknown")
else:
    print(highest - lowest)
