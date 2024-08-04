#collect input from the user
#use if statement to check if the number is divisible by 5, 6 or both

user_input = int(input('Enter a number: '))

if user_input % 5 == 0 and user_input % 6 == 0:
    print(f'is {user_input} divisible by 5 and 6? false')
if user_input % 5 == 0 or user_input % 6 == 0:
    print(f'is {user_input} divisible by 5 or 6? True')
if user_input % 5 == 0 or user_input % 6 == 0:
    print(f'is {user_input} divisible by 5 or 6, but not both? True')
