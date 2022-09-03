t = int(input())

boards = []
for board in range(t):
    boards.append(list(map(int, input().split(" "))))

for board in boards:
    w, h = board
    if w >= 4 and h >= 2:
        print("good")
    elif h >= 4 and w >= 2:
        print("good")
    elif w >= 7:
        print("good")
    else:
        print("bad")
