number = int(input('Enter a number you want to print the multiplication table: '))

for count in range(1,11):
    print(f'{number} * {count} = {number * count}')
