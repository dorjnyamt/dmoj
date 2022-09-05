next_number = int(input())

late_students = 0
waiting_students = 0
stats = []

while True:
    command = input()
    if command == "TAKE":
        next_number = next_number + 1
        late_students = late_students + 1
        waiting_students = waiting_students + 1
    elif command == "SERVE":
        waiting_students = waiting_students - 1
    elif command == "CLOSE":
        stats.append((late_students, waiting_students, next_number))
        late_students = 0
        waiting_students = 0
    elif command == "EOF":
        break

    if next_number == 1000:
        next_number = 1
    
for stat in stats:
    late_students, waiting_students, next_number = stat
    print(late_students, waiting_students, next_number)