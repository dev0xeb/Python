
from random import randint

print('Welcome to Clinton guess game')

guess_number = randint(1, 1000)
counter = 0
user_input = 0
decision = 0


while decision != 'no' and decision != 'No':
    user_input = int(input('Enter a number between 1 - 1000: '))
    counter+=1
    if user_input > guess_number:
        print('Too high, try again')
    elif user_input < guess_number:
        print('Too low, try again')
    elif user_input == guess_number:
        print('Congratulations, you guessed the number')
        
        decision = str(input('Do you want to continue the game. Enter any key to continue or No: '))
        guess_number = randint(1, 1000)
