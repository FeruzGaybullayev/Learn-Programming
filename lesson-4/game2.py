# Bonus Challenge
import random
choose = ['rock', 'paper', 'scissors']


counter = 1

user, computer = 0, 0

while True:
    if True:
        computer_choose = random.choice(choose)
    user_choose = input('Choose one of the three (rock, paper, or scissors): ')

    if choose == user_choose:
        print('User:', user, 'Computer', computer)

    elif computer_choose == 'rock': 
        if user_choose == 'paper':
            user += 1
            print('User:', user, 'Computer', computer)
        else:
            computer += 1
            print('User:', user, 'Computer', computer)
    elif computer_choose == 'paper':
        if user_choose == 'rock':
            computer += 1
            print('User:', user, 'Computer', computer)
        else:
            user += 1
            print('User:', user, 'Computer', computer)

    counter += 1
    if counter == 6:
        break

print(f'''
Game is over:
User: {user} 
Computer: {computer}
''')
if user > computer:
    print('User Win')
elif user < computer:
    print('Computer Win')
else:
    print('Equal')