holder = input()
duels = int(input())

holders = {holder}
for duel in range(duels):
    winner, loser = input().split(" ")
    if loser == holder:
        holder = winner
        holders.add(holder)

print(holder)
print(len(holders))