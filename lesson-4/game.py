# 4. Number Guessing Game Create a simple number guessing game.

import random
number = random.randint(1, 100)
player = int(input('Guess number 1 to 100: '))
counter = 1

response = {'Y', 'YES', 'y', 'yes', 'ok'}
while True:
    if player == number:
        print("You guessed it right!")
        break

    elif player > number and (player - number) >= 15:
        player = int(input("Too high! "))
        
    elif player > number:
        player = int(input('Try again: '))

    elif player < number and (number - player) >= 15:
        player = int(input("Too low! "))

    elif player < number:
        player = int(input('Try again: '))

    counter += 1

    if counter == 10:
        print("You lost. Want to play again? ")
        res = input('If you want to play again enter Y, y, YES, yes or ok: ')
        
        if res in response:
            counter = 1
        else:
            break
