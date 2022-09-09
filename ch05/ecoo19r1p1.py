for dataset in range(10):
    clean, n_event, days = map(int, input().split())
    d_events = list(map(int, input().split(" ")))
    d_events.sort()
    laundry = 0
    event = 0
    total = clean
    for day in range(days):
        if clean == 0:
            laundry += 1
            clean = total

        while event < len(d_events) and (d_events[event] == day + 1):
            total += 1
            clean += 1
            event += 1

        clean -= 1
    print(laundry)

    