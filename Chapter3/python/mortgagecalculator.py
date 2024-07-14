principal = int(input('Enter the amount the client wishes to borrow: '))
annual_interest_rate = int(input('Enter the yearly interest offered on the mortgage: '))
duration = int(input('Enter the duration of the loan in years: '))

monthly_interest_rate =  (annual_interest_rate/100) / 12
print('the monthly interest rate is ', monthly_interest_rate)

loan_term_in_months = duration * 12
print('the loan term in months is ', loan_term_in_months)

client_monthly_payment = principal *(monthly_interest_rate *(1 + monthly_interest_rate )**loan_term_in_months) / ((1 + monthly_interest_rate)**loan_term_in_months -1)
print('your monthly payment is ', client_monthly_payment)
