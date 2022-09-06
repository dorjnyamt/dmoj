n = int(input())

for i in range(n):
    line = input()
    encoded = ""
    prev = line[0]
    freq = 0
    for pos, char in enumerate(line):
        if char != prev or pos == len(line) - 1:
            encoded = encoded + f"{freq} {prev} "
            prev = char
            freq = 1
        if char == prev:
            freq = freq + 1

    print(encoded.strip())