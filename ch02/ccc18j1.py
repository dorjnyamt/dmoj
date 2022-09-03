digit_1 = int(input())
digit_2 = int(input())
digit_3 = int(input())
digit_4 = int(input())

if (
    (digit_1 == 8 or digit_1 == 9)
    and (digit_4 == 8 or digit_4 == 9)
    and (digit_2 == digit_3)
):
    print("ignore")
else:
    print("answer")
