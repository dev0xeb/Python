age = int(input("enter your age: "))
if age > 20 and age <=45:
	print('you are eligible')
	print('to go')
	print('to the strip club')

elif age >= 13 and age <=19:
	print('you are a wimp')
	print('go read a book')

elif age > 0 and  age < 13:
	print('you are still a child')
	print('go back home')

else:
	print('go to the old peeps club')