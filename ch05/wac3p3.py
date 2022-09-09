moves = input()
n_combo = int(input())
combos = []
points = 0
for each in range(n_combo):
    move, point = input().split()
    point = int(point)
    combos.append((move, point))
combos.sort(key=lambda move: len(move[0]), reverse=True)

print(combos)

    # if combo[0] in moves:
    #     points += int(combo[1])
    #     where = moves.index(combo[0]) + len(combo[0])
    #     print(f"Move is {combo[0]}. Move is found at {where} and starting {moves[where:]}.")
    #     moves = moves[where + 1:]
    #     print(f"Moves is now {moves}.")