#collect number of feet from user
# multiply the number of feet from the user by the 0.305 which therefore gives the value of whatever the user entered in meters


number_in_feet = int(input('Enter a number in feet to convert it to meters: '))

number_in_meters = number_in_feet * 0.305

print(f'The conversion of {number_in_feet} to meters is {number_in_meters}')
