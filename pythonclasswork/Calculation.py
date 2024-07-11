password = input("enter your password: ")

password = len(password) * '*'
print (password)


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

print ('your full name is', first_name,  last_name,  'and your age is', age)


message = ''' my name is devoxeb
my bestfriend is dev0xjay
he is my dawg'''

print(message)


name = input("enter your name: ")
if name:
	print('your name is', name)
	print('hello')
	print('i am nice')


age = int(input("enter your age: "))
if age >= 18:
	print('you are eligible')
	print('to go')
	print('to the strip club')
else:
	print('go back home')