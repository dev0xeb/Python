sentinel = -1
total_miles = 0
total_gallons = 0
total_miles_gallon = 0
count_trips = 0

while True:
    gallons_used = float(input('Enter the gallons used (-1 to end): '))
    if gallons_used == sentinel:
        print('end of input')
        break
    
    miles_driven = float(input('Enter the number of miles driven: '))
    miles_per_gallon = miles_driven / gallons_used
    print('the miles/gallon for this tank was', miles_per_gallon)
   
    total_gallons += gallons_used
    total_miles += miles_driven
    count_trips +=1
    total_miles_gallon += miles_per_gallon
    
print('total gallons used is ', total_gallons)
print('total miles driven is ', total_miles)

average_miles_gallon = total_miles_gallon / count_trips
print('the overall average miles/gallon was ', average_miles_gallon)
    
    
