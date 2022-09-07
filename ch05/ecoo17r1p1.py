COSTS_BY_YEAR = [12, 10 , 7, 5]

for i in range(10):
    trip_cost = int(input())
    student_ratios = list(map(float, input().split(" ")))
    students = int(input())
    students_per_year = list(map(lambda x: x * students, student_ratios))
    students_per_year = list(map(int, students_per_year))
    total_raised = 0
    counted = sum(students_per_year)
    uncounted = students - counted
    most = max(students_per_year)
    where = students_per_year.index(most)
    students_per_year[where] = students_per_year[where] + uncounted

    for i in range(len(students_per_year)):
        total_raised = total_raised + students_per_year[i] * COSTS_BY_YEAR[i]
    
    if total_raised / 2 < trip_cost:
        print("YES")
    else:
        print("NO")
