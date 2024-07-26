#collect the number of mintues from user
#To calculate the amount mintues in a year is 60 monutes * 24 which is 1440, 1440 * 365 is 525600 which is how many minutes in a year
#to get the number of years, the number of minutes entered by the user will be divied by the number of minutes in a year(525600)
#to get the number of days, the number of minutes entered by the user is divided by the number of minutes in a day 1440 and it's divided by the result from number in a year to get the remaining days.


minutes = int(input('Enter the number of minutes: '))

number_of_years = minutes // 525600
number_of_days = (minutes / 1440) % number_of_years
print(f'{number_of_years} of years and {number_of_days} days')
