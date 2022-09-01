burgers = [461, 431, 420, 0]
drinks = [130, 160, 118, 0]
sides = [100, 57, 70, 0]
desserts = [167, 266, 75, 0]

burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

print(f"Your total Calorie count is {burgers[burger - 1] + drinks[drink - 1] + sides[side - 1] + desserts[dessert - 1]}.")