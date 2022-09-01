apple_three_pointers = int(input())
apple_two_pointers = int(input())
apple_free_throws = int(input())
banana_three_pointers = int(input())
banana_two_pointers = int(input())
banana_free_throws = int(input())

apple_total = apple_three_pointers * 3 + apple_two_pointers * 2 + apple_free_throws
banana_total = banana_three_pointers * 3 + banana_two_pointers * 2 + banana_free_throws

if apple_total > banana_total:
    print('A')
elif apple_total < banana_total:
    print('B')
else:
    print('T')