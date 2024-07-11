count = 0
user_input = 0
total_deposit = 0

while user_input != -1:
    print('1.Deposit', '\n', '2. Withdraw', '\n', '3.Balance')

    user_input = int(input('Enter a number: '))

    if user_input ==1:
        deposit = int(input('Enter a deposit amount: '))
        total_deposit += deposit
                
    elif user_input == 2:
        withdraw = int(input('Enter a withdrawal amount: '))
        if withdraw > total_deposit:
            print('invalid amoount input')
        else:
            print('Withdrawal successful')
    elif user_input == 3:
        balance = total_deposit - withdraw
        print(balance)

    else:
        break

            

    
