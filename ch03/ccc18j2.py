n = int(input())
old_capacity = input()
new_capacity = input()

occupied = 0

for i in range(0, len(old_capacity)):
    if old_capacity[i] == new_capacity[i] and old_capacity[i] == 'C':
        occupied = occupied + 1

print(occupied)
