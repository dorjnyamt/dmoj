word = ""

while word != "quit!":
    word = input()
    if len(word) > 4 and word[-2:] == "or" and word[-3] in "qwrtypsdfghjklzxcvbnm":
        print(word[:-2] + "our")
    elif word == "quit!":
        break
    else:
        print(word)