paint = int(input())
bottlecap = int(input())
dollar = int(input())

n_bottlecaps = paint // bottlecap
p_bottlecaps = n_bottlecaps * dollar

price = p_bottlecaps + (paint % bottlecap)

print(price)

