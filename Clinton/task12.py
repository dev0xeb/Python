user_input = int(input('Enter 0 to convert from U.S dollars to Nigerian Naira and 1 to convert from Nigerian Nairs to U.S dollars: '))
if user_input == 1:
    dollar_amount = int(input('Enter the amount of dollar you wish to convert to naira: '))
    amount_in_naira = dollar_amount * 1500
    print(f'The amount of {dollar_amount} dollars to Naira is {amount_in_naira}')
if user_input == 0:
    naira_amount = int(input('Enter the amount of naira you wish to convert to dollar: '))
    amount_in_dollars = user_input / 1500
    print(f'The amount of {amount_in_dollars} dollars to Naira is {amount_in_dollars:.3f}')
