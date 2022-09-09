moves = input()
n_combo = int(input())
combos = []
for each in range(n_combo):
    move, point = input().split()
    point = int(point)
    combos.append((move, point))
combos.sort(key=lambda move: len(move[0]), reverse=True)

points = len(moves)
step = 0
while step < len(moves):
    # print(f"START Step is now {step} and point is {points} and rest are {moves[step:]}")
    longest = 0
    for combo in combos:
        if combo[0] in moves[step:step + len(combo[0])]:
            # print(f"combo {combo[0]} found at {moves[step:step + len(combo[0])]}")
            longest = len(combo[0]) - 1
            points += combo[1]
            break
    step = step + longest + 1

print(points)
