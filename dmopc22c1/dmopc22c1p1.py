import sys
tests = int(input())
for test in range(tests):
    n = int(input())
    seq = list(map(int, sys.stdin.readline.split()))
    substitute = 10 ** 9
    result = True
    new_seq = []
    new_seq.append(seq[0])
    alternate = False
    for i in range(1, n - 1):
        if seq[i] == 0:
            if seq[i - 1] < substitute > seq[i + 1]:
                new_seq.append(substitute)
            elif seq[i - 1] > substitute < seq[i + 1]:
                new_seq.append(substitute)
        else:
            new_seq.append(seq[i])
        substitute = -substitute
    
    new_seq.append(seq[-1])

    for i in range(1, n - 1):
        if not (new_seq[i - 1] < new_seq[i] > new_seq[i + 1] or new_seq[i - 1] > new_seq[i] < new_seq[i + 1]):
            result = False

    if result:
        print("YES")
    else:
        print("NO")
