password = input()

uppercase = 0
lowercase = 0
numeral = 0

for char in password:
    if char.isupper():
        uppercase = uppercase + 1
    elif char.islower():
        lowercase = lowercase + 1
    else:
        numeral = numeral + 1

if len(password) < 8 or len(password) > 12:
    print("Invalid")
elif uppercase > 1 and lowercase > 2 and numeral > 0:
    print("Valid")
else:
    print("Invalid")