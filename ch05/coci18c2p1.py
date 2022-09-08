scores_halftime = 0
scores = []
a = int(input())
for score in range(a):
    time = int(input())
    scores.append([time, "A"])
    if time <= 1440:
        scores_halftime += 1

b = int(input())
for score in range(b):
    time = int(input())
    scores.append([time, "B"])
    if time <= 1440:
        scores_halftime += 1

scores.sort()
turnaround = 0
a_score = 0
b_score = 0
winner = scores[0][1]
old_winner = scores[0][1]
for score in scores:
    if score[1] == "A":
        a_score += 1
    elif score[1] == "B":
        b_score += 1
    if a_score > b_score:
        winner = "A"
    elif a_score < b_score:
        winner = "B"
    # else:
        # print(f"It is a tie: {a_score} vs. {b_score}")
    if old_winner != winner:
        # print(f"It is a turnaround: {a_score} vs. {b_score}")
        turnaround += 1
        old_winner = winner
    # print(f"Current score {a_score} vs. {b_score}. Winner is {winner}.")
    
print(scores_halftime)
print(turnaround)