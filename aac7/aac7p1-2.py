t = int(input())

for board in range(t):
    w, h = map(int, input().split(" "))
    if w >= 4:
        if w >= 7 or h >= 2:
            print("good")
    elif h >= 4:
        if h >= 7 or w >= 2:
            print("good")
    else:
        print("bad")