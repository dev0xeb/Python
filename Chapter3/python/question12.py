user_input = int(input('Enter a five digit integer: '))
if user_input < 10000 or user_input > 99999:
    user_input = int(input('Enter a five digit integer: ')) 

first_num = user_input // 10000
second_num = (user_input // 1000) % 10
third_num = (user_input // 100)%10
fourth_num = (user_input //10)%10
fifth_num = user_input % 10

if first_num == fifth_num and second_num == fourth_num:
    print("Number is a palindrome")
else:
    print('Number is not a palindrome')
    
