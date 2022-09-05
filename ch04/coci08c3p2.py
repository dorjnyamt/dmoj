encoded = input()
i = 0
decoded = ""

while i < len(encoded):
    decoded = decoded + encoded[i]
    if encoded[i] in "aeiou":
        i = i + 3
    else:
        i = i + 1

print(decoded)