#collect inputs
#calculate the gross pay
#calculate the federal witholding
#calculate the state witholding
#calculate the total deduction
#calculate the net pay


employee_name = input('Enter employee\'s name: ')
hours_worked = int(input('Enter number of hours worked in a week: '))
hourly_pay_rate = float(input('Enter hourly pay rate: '))
federal_tax = int(input('Enter federal tax withholding rate: '))
state_tax = int(input('Enter state tax witholding rate: '))

gross_pay = hours_worked * hourly_pay_rate
print(f'Gross pay is; {gross_pay}')

print('Deductions')
federal_witholding = federal_tax * gross_pay
print(f'Federal witholding is: {federal_witholding}')

state_witholding = state_tax * gross_pay
print(f'state witholding is: {state_witholding}')

total_deduction = federal_witholding + state_witholding
print(f'total deduction: {total_deduction}')

net_pay = gross_pay - federal_witholding + state_witholding
print(f'net pay is {net_pay}')

