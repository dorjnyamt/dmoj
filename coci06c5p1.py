moves = input()
location = 1

for move in moves:
    if move == 'A':
        if location == 1:
            location = 2
        elif location == 2:
            location = 1
    if move == 'B':
        if location == 2:
            location = 3
        elif location == 3:
            location = 2
    if move == 'C':
        if location == 3:
            location = 1
        elif location == 1:
            location = 3

print(location)