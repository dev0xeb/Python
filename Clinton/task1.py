#collect input of radius and length from the user
#intialize pi as 3.14
#calculate the area of the cylinder by multiplying pi and the radius collected from the user and then raise to power of two
#calculate the volume of the cylinder by multiplying the answer gotten from the area of the cylinder by the length collected from the user
#print the calculated values of the area and length


pi = 3.14
radius = int(input('Enter the radius of a cylinder: '))
length = int(input('Enter the length of the cylinder: '))

area = (pi*radius)**2
volume = area * length

print(f'The area of the cylinder is {area}')
print(f'The volume of the cylinder is {volume}')
