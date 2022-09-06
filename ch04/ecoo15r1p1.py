for i in range(10):
    orange, blue, green, yellow, pink, violet, brown, red = 0, 0, 0, 0, 0, 0, 0, 0
    time = 0

    while True:
        smartie = input()
        if smartie == "orange":
            orange = orange + 1
        elif smartie == "blue":
            blue = blue + 1
        elif smartie == "green":
            green = green + 1
        elif smartie == "yellow":
            yellow = yellow + 1
        elif smartie == "pink":
            pink = pink + 1
        elif smartie == "violet":
            violet = violet + 1
        elif smartie == "brown":
            brown = brown + 1
        elif smartie == "red":
            red = red + 1
        elif smartie == "end of box":
            time = time + ((orange + 6) // 7) * 13
            time = time + ((blue + 6) // 7) * 13
            time = time + ((green + 6) // 7) * 13
            time = time + ((yellow + 6) // 7) * 13
            time = time + ((pink + 6) // 7) * 13
            time = time + ((violet + 6) // 7) * 13
            time = time + ((brown + 6) // 7) * 13
            time = time + red * 16
            break

    print(time)

        