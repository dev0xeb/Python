#collect values of gratuity and subtotal from to user
#to calculate the gratuity,(gratuity_rate/100)*10. it is firstly divided by 100 because it is in percentage and mumltiplied by 10
#the total is the addition of the gratuity and the subtotal


gratuity_rate = int(input('Enter the gratuity rate value: '))
subtotal = int(input('Enter the subtotal value: '))

gratuity = (gratuity_rate / 100) * 10
total = subtotal + gratuity

print(f'the gratuity is {gratuity} and the total is {total}')
