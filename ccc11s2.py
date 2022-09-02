n = int(input())

answer = []
correct = 0

for i in range(2 * n):
    answer.append(input())

for i in range(n):
    if answer[i] == answer[n + i]:
        correct = correct + 1

print(correct)
