number = 0
for count in range(10):
    user_input = int(input(f'Enter number {count+1}: '))
    print('you entered', user_input)
    if user_input > number:
        number = user_input
print('the greatest number is', number)
