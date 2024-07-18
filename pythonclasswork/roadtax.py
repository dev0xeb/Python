user_input = int(input('Enter the amount of the car: '))
if user_input < 1000000:
    print(f'your Road Tax of 10% is {user_input * 0.1}')


if user_input >= 1000000 and user_input < 3000000:
    print(f'your Road Tax of 15% is {user_input * 0.15}')
    
if user_input >= 3000000 and user_input < 5000000:
    print(f'your Road Tax of 20% is {user_input * 0.2}')

if user_input >= 5000000:
    print(f'your Road Tax of 25% is {user_input * 0.25}')

