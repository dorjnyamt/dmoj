coins = int(input())
machine_1 = int(input())
machine_2 = int(input())
machine_3 = int(input())

times = 0
machine = 1
while coins > 0:
    coins = coins - 1
    times = times + 1

    if machine == 1:
        machine_1 = machine_1 + 1
        if machine_1 == 35:
            machine_1 = 0
            coins = coins + 30
        machine = 2
    elif machine == 2:
        machine_2 = machine_2 + 1
        if machine_2 == 100:
            machine_2 = 0
            coins = coins + 60
        machine = 3
    elif machine == 3:
        machine_3 = machine_3 + 1
        if machine_3 == 10:
            machine_3 = 0
            coins = coins + 9
        machine = 1

print(f"Martha plays {times} times before going broke.")   