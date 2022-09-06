n = int(input())

for i in range(n):
    line = input()
    encoded = ""
    prev = line[0]
    freq = int(0)
    for pos, char in enumerate(line):
        if char != prev:
            encoded = encoded + f"{int(freq)} {prev} "
            prev = char
            freq = 1
        elif char == prev:
            freq = freq + 1
        if pos == len(line) - 1:
            encoded = encoded + f"{int(freq)} {prev} "

    print(encoded.strip())