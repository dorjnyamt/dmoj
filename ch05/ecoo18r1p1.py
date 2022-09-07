for dataset in range(10):
    t, n = map(int, input().split())
    days = []
    most = 0
    for day in range(n):
        box = input()
        if box == 'E':
            days.append(most)
        elif box == 'B':
            if day > most:
                most = day + t
            else:
                most = most + t
            days.append(most)
    
    diff = max(days) - n
    if diff > 0:
        print(diff)
    else:
        print(0)