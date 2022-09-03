n = int(input())

letters = "A"

for i in range(n):
    new_letters = ""
    for char in letters:
        if char == "A":
            new_letters = new_letters + "B"
        else:
            new_letters = new_letters + "BA"
    letters = new_letters
    print(letters)

a = letters.count("A")
b = letters.count("B")

print(a, b)