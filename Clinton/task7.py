#intialize all value given
#calculate the intial amount deposit with th formula given


final_account_value = 5000
monthly_interest_rate = 0.05 #a monthly interest rate of 5%
number_of_month = 36 #12 months in a year, and saving for 3 years which gives us 12*3

intial_deposit_amount = final_account_value // ((1 + monthly_interest_rate)**number_of_month)
print(f'the intial deposit amount is {intial_deposit_amount}')
