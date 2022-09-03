number = int(input())

if (number == 1):
    print('A long time ago in a galaxy far away...')
else:
    print('A long time ago in a galaxy ' + 'far, ' * (number - 1) +'far away...')