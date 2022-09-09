moves = input()
n_combo = int(input())
combos = []
points = 0
for each in range(n_combo):
    move, point = input().split()
    point = int(point)
    combos.append((move, point))
combos.sort(key=lambda move: len(move[0]), reverse=True)

points = len(moves)
step = 0
while step < len(moves):
    # print(f"START Step is now {step} and point is {points}")
    longest = 1
    highest = 0
    found = False
    for combo in combos:
        if found or len(moves) < len(combo[0]) + step:
            break
        j=0
        k=step
        while j < len(combo[0]) and k < len(moves):
            if combo[0][j] == moves[k]:
                j += 1
                k += 1
                if j == len(combo[0]) - 1:
                    # print(f"Combo {combo[0]} found at {step}")
                    found = True
                    longest = len(combo[0])
                    highest = combo[1]
                    # print(f"Longest is now {longest}")
            else:
                # print(f"{combo[0]} is not found in moves {moves[step:]}")
                break

    points += highest
    step = step + longest

print(points)