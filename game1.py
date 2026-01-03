import random

count = 3
ans = random.randint(1, 10)
while count > 0:
    count = count - 1
    temp = input('guess:')
    guess = int(temp)
    if guess == ans:
        print('y')
    else:
        if guess > ans:
            print('big')
        else:
            print('small')

print('end')
