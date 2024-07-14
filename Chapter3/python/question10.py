amount_invested = 1000
annual_return = 7/100

total =0

for years in range(0,30):
    amount_deposited = amount_invested *(1 + annual_return)** years
    print(amount_deposited)
print(f'the amount after 30 years is , {amount_deposited: .2f}')
