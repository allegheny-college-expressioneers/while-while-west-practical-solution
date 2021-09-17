import random

random_number = int(random.random() * 100 + 1)
while True:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess < random_number:
        print('Too low...')
    elif guess > random_number:
        print('Too high...')
    else:
        print('You got it!')
        break

# Another correct implementation
random_number = int(random.random() * 100 + 1)
while True:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess == random_number:
        print('You got it!')
        break
    if guess < random_number:
        print('Too low...')
    else:
        print('Too high...')

