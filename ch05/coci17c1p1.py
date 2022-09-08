cards = [0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 12, 4]
drawn = int(input())

point = 0

for draw in range(drawn):
    card = int(input())
    point = point + card
    cards[card] = cards[card] - 1

diff = 21 - point
more = sum(cards[diff:])
less = 52 - drawn - more

if more >= less:
    print("DOSTA")
else:
    print("VUCI")