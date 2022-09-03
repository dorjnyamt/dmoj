a = int(input())
b = int(input())
c = int(input())

if a > b:
    if b > c:
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)
elif b > c:
    if a > c:
        print(a)
    else:
        print(c)
else:
    print(b)

