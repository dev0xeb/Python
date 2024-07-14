total = 0
average = 0
product = 0

numbers =[]
for count in range(3):
    user_input= int(input('Enter a number: '))
    print('you entered', user_input)
    numbers.append(user_input)
    total += user_input
    average = total / 3
    product *=user_input
print('the product is ', product)
print('the total is ', total)
print('the average is ', average)

minimum_number = min(numbers)
maximum_number = max(numbers)
print('the smallest number is ', minimum_number, 'the largest number is ', maximum_number)
