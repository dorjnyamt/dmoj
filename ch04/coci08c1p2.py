n = int(input())
answers = input()
# ABC
# BABC
# CCAABB
adrian, bruno, goran = 0, 0, 0
for index, answer in enumerate(answers):
    if index % 3 == 0:
        if answer == 'A':
            adrian = adrian + 1
    elif index % 3 == 1:
        if answer == 'B':
            adrian = adrian + 1
    elif index % 3 == 2:
        if answer == 'C':
            adrian = adrian + 1
    
    if index % 4 == 0:
        if answer == 'B':
            bruno = bruno + 1
    elif index % 4 == 1:
        if answer == 'A':
            bruno = bruno + 1
    elif index % 4 == 2:
        if answer == 'B':
            bruno = bruno + 1
    elif index % 4 == 3:
        if answer == 'C':
            bruno = bruno + 1
    
    if index % 6 == 0:
        if answer == 'C':
            goran = goran + 1
    elif index % 6 == 1:
        if answer == 'C':
            goran = goran + 1
    elif index % 6 == 2:
        if answer == 'A':
            goran = goran + 1
    elif index % 6 == 3:
        if answer == 'A':
            goran = goran + 1
    elif index % 6 == 4:
        if answer == 'B':
            goran = goran + 1
    elif index % 6 == 5:
        if answer == 'B':
            goran = goran + 1

winner = max(adrian, bruno, goran)
print(winner)

if winner == adrian:
    print('Adrian')
if winner == bruno:
    print('Bruno')
if winner == goran:
    print('Goran')