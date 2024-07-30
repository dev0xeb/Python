#collect input from users
#walk through the input using a loop to count the characters inputted

user_input = input('Enter your values: ')
print(user_input)
counter = 0
for count in range (len(user_input)):
    counter = counter + 1
print(f'Letters is {counter}')
