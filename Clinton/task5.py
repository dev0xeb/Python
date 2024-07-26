#collect input from user and put a conditional satement that states that if the digit entered by the user is greater than 1000 the user should re-input
#using the % and / operator to seperate the digits of whether the digit is a single, double, or triple integer
#add each values after the seperation


user_input = int(input('Enter a number between 0 - 1000: '))
if user_input  < 0 or user_input > 1000:
    user_input = int(input('Inavlid input, try again. Enter a number between 0 - 1000: '))
    
if user_input  > 0 and user_input <= 9:
    print(f'the sum of all its digit is {user_input}')
    
elif user_input >=10 and user_input <=99:
    num1 = user_input // 10
    num2 = user_input % 10
    addition = num1 + num2
    print(f'the sum of all its digit is {addition}')

elif user_input >=100 and user_input <=999:
    num1 = user_input // 100
    num2 = (user_input // 10)% 10
    num3 = user_input % 10
    addition = num1 + num2 + num3
    print(f'the sum of all its digit is {addition}')
else:
    print('1')
