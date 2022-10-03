NUM_CARDS = 52
HIGH_CARDS = ["jack", "queen", "king", "ace"]


def check_if_not_high(cards):
    for card in cards:
        if card in HIGH_CARDS:
            return False

    return True


cards = []

for i in range(NUM_CARDS):
    card = input()
    cards.append(card)

player_a = 0
player_b = 0
player = "A"
card = 0

while card < len(cards):
    points = 0
    remaining = NUM_CARDS - card - 1
    if (
        cards[card] == "jack"
        and remaining >= 1
        and check_if_not_high(cards[card + 1 : card + 2])
    ):
        points = 1
    if (
        cards[card] == "queen"
        and remaining >= 2
        and check_if_not_high(cards[card + 1 : card + 3])
    ):
        points = 2
    if (
        cards[card] == "king"
        and remaining >= 3
        and check_if_not_high(cards[card + 1 : card + 4])
    ):
        points = 3
    if (
        cards[card] == "ace"
        and remaining >= 4
        and check_if_not_high(cards[card + 1 : card + 5])
    ):
        points = 4

    if points > 0:
        print(f"Player {player} scores {points} point(s).")

    if player == "A":
        player_a = player_a + points
        player = "B"
    else:
        player_b = player_b + points
        player = "A"

    card += 1

print(f"Player A: {player_a} point(s).")
print(f"Player B: {player_b} point(s).")
