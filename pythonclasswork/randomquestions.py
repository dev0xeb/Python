from random import randint
Correct = 0
Incorrect = 0
num1 = randint(1, 10)
num2 = randint(1, 50)
for task in range(10):
    num1 = randint(1, 10)
    num2 = randint(1, 50)
    print(f'{num1} + {num2}')
    user_input = int(input('ADD the numbers? '))
    if user_input == num1 + num2:
        print('Correct')
        Correct+=1
    else:
        print('Incorrect')
        Incorrect+=1
print(f'You got {Correct} question right and missed {Incorrect} question over 10 questions')
