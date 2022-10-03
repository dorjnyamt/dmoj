cards = []
for i in range(52):
    card = input()
    cards.append(card)
card = 0
player_a = 0
player_b = 0
high_cards = ["jack", "queen", "king", "ace"]

print(cards)
while card < len(cards):
    if cards[card] == "jack" and card < len(cards) - 1 and cards[card + 1] not in high_cards:
        if card % 2 == 0:
            player_a += 1
            print(f"Player A scores {1} point(s).")
        else:
            player_b += 1
            print(f"Player A scores {1} point(s).")
    card += 1

print(f"Player A scores {player_a} point(s).")
print(f"Player B scores {player_b} point(s).")
