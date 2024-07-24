tax = 0
first_tax = 0
second_tax = 0
third_tax = 0
fourth_tax = 0
fifth_tax = 0
sixth_tax = 0

print('welcome to the United States Tax Commission')

user_input = int(input('There are 4 filing status. Enter 0 for single filers \n 1 for Married Filling Jointly \n 2 for Married filling separately \n 3 for Head of Household: ' ))
taxable_income = float(input('Enter your taxable income here: '))

if user_input == 0:
    if taxable_income <= 8350:
        tax = taxable_income * 0.10
        print(f'your tax for single filers is {tax:.2f}')
        
    elif taxable_income >= 8351 and taxable_income <= 33950:
        first_tax = 8350 * 0.10
        second_tax = (taxable_income - 8350) - 0.15
        tax = first_tax + second_tax
        print(f'your tax for single filers is {tax:.2f}')
        
    elif taxable_income >= 33951 and taxable_income <= 82250:
        first_tax = 8350 * 0.10
        second_tax = (33950 - 8350) * 0.15
        third_tax = (taxable_income - 33950) * 0.25
        tax = first_tax + second_tax + third_tax
        print(f'your tax for single filers is {tax:.2f}')

    elif taxable_income >= 82251 and taxable_income <= 171550:
        first_tax = 8350 * 0.10
        second_tax = (33950 - 8350) * 0.15
        third_tax = (82250 -  33950) * 0.25
        fourth_tax = (taxable_income - 82250) * 0.28
        tax = first_tax + second_tax + third_tax + fourth_tax
        print(f'your tax for single filers is {tax:.2f}')

    elif taxable_income >= 171551 and taxable_income <= 372950:
        first_tax = 8350 * 0.10
        second_tax = (33950 - 8350) * 0.15
        third_tax = (82250 - 33950) * 0.25
        fourth_tax = (171550 - 82250) * 0.28
        fifth_tax = (taxable_income - 171550) * 0.33
        tax = first_tax + second_tax + third_tax + fourth_tax + fifth_tax
        print(f'your tax for single filers is {tax:.2f}')

    elif taxable_income >= 372951:
        first_tax = 8350 * 0.10
        second_tax = (33950 - 8350) * 0.15
        third_tax = (82250 - 33950) * 0.25
        fourth_tax = (171550 - 82250) * 0.28
        fifth_tax = (372950 -171550) * 0.33
        sixth_tax = (taxable_income - 372950) * 0.35
        tax = first_tax + second_tax + third_tax + fourth_tax + fifth_tax + sixth_tax
        print(f'your tax for single filers is {tax:.2f}')

    
elif user_input == 1:
    if taxable_income <= 16700:
        tax = taxable_income * 0.10
        print(f'your tax for Married Filling Jointly is {tax:.2f}')
        
    elif taxable_income >= 16701 and taxable_income <= 67900:
        first_tax = 16700 * 0.10
        second_tax = (taxable_income - 16700) - 0.15
        tax = first_tax + second_tax
        print(f'your tax for Married Filling Jointly is {tax:.2f}')
        
    elif taxable_income >= 67901 and taxable_income <= 137050:
        first_tax = 16700 * 0.10
        second_tax = (67900 - 16700) * 0.15
        third_tax = (taxable_income - 67900) * 0.25
        tax = first_tax + second_tax + third_tax
        print(f'your tax for Married Filling Jointly is {tax:.2f}')

    elif taxable_income >= 137051 and taxable_income <= 208850:
        first_tax = 16700* 0.10
        second_tax = (67900 - 16700) * 0.15
        third_tax = (137050 -  67900) * 0.25
        fourth_tax = (taxable_income - 137050) * 0.28
        tax = first_tax + second_tax + third_tax + fourth_tax
        print(f'your tax for Married Filling Jointly is {tax:.2f}')

    elif taxable_income >= 208851 and taxable_income <= 372950:
        first_tax = 16700 * 0.10
        second_tax = (67900 - 16700) * 0.15
        third_tax = (137050 - 67900) * 0.25
        fourth_tax = (208850 - 137050) * 0.28
        fifth_tax = (taxable_income - 208850) * 0.33
        tax = first_tax + second_tax + third_tax + fourth_tax + fifth_tax
        print(f'your tax for Married Filling Jointly is {tax:.2f}')

    elif taxable_income >= 372951:
        first_tax = 16700 * 0.10
        second_tax = (67900 - 816700) * 0.15
        third_tax = (137050 - 67900) * 0.25
        fourth_tax = (208850 - 137050) * 0.28
        fifth_tax = (372950 -208850) * 0.33
        sixth_tax = (taxable_income - 372950) * 0.35
        tax = first_tax + second_tax + third_tax + fourth_tax + fifth_tax + sixth_tax
        print(f'your tax for Married Filling Jointly is {tax:.2f}')

        
elif user_input == 2:
    if taxable_income <= 8350:
        tax = taxable_income * 0.10
        print(f'your tax for Married filling separately is {tax:.2f}')
        
    elif taxable_income >= 8351 and taxable_income <= 33950:
        first_tax = 8350 * 0.10
        second_tax = (taxable_income - 8350) - 0.15
        tax = first_tax + second_tax
        print(f'your tax for Married filling separately is {tax:.2f}')
        
    elif taxable_income >= 33951 and taxable_income <= 68525:
        first_tax = 8350 * 0.10
        second_tax = (33950 - 8350) * 0.15
        third_tax = (taxable_income - 33950) * 0.25
        tax = first_tax + second_tax + third_tax
        print(f'your tax for Married filling separately is {tax:.2f}')

    elif taxable_income >= 68526 and taxable_income <= 104425:
        first_tax = 8350 * 0.10
        second_tax = (33950 - 8350) * 0.15
        third_tax = (68525 -  33950) * 0.25
        fourth_tax = (taxable_income - 68525) * 0.28
        tax = first_tax + second_tax + third_tax + fourth_tax
        print(f'your tax for Married filling separately is {tax:.2f}')

    elif taxable_income >= 104426 and taxable_income <= 186475:
        first_tax = 8350 * 0.10
        second_tax = (33950 - 8350) * 0.15
        third_tax = (68525 - 33950) * 0.25
        fourth_tax = (104425 - 68525) * 0.28
        fifth_tax = (taxable_income - 104425) * 0.33
        tax = first_tax + second_tax + third_tax + fourth_tax + fifth_tax
        print(f'your tax for Married filling separately is {tax:.2f}')

    elif taxable_income >= 185476:
        first_tax = 8350 * 0.10
        second_tax = (33950 - 8350) * 0.15
        third_tax = (68525 - 33950) * 0.25
        fourth_tax = (104425 - 68525) * 0.28
        fifth_tax = (186475 - 104425) * 0.33
        sixth_tax = (taxable_income - 186475) * 0.35
        tax = first_tax + second_tax + third_tax + fourth_tax + fifth_tax + sixth_tax
        print(f'your tax for Married filling separately is {tax:.2f}')
    

elif user_input == 3:
    if taxable_income <= 11950:
        tax = taxable_income * 0.10
        print(f'your tax for Head of Household is {tax:.2f}')
        
    elif taxable_income >= 11951 and taxable_income <= 45500:
        first_tax = 11950 * 0.10
        second_tax = (taxable_income - 11950) - 0.15
        tax = first_tax + second_tax
        print(f'your tax for Head of Household is {tax:.2f}')
        
    elif taxable_income >= 25501 and taxable_income <= 117450:
        first_tax = 11950 * 0.10
        second_tax = (45500 - 11950) * 0.15
        third_tax = (taxable_income - 45500) * 0.25
        tax = first_tax + second_tax + third_tax
        print(f'your tax for Head of Household is {tax:.2f}')

    elif taxable_income >= 117451 and taxable_income <= 190200:
        first_tax = 11950 * 0.10
        second_tax = (45500 - 11950) * 0.15
        third_tax = (117450 -  45500) * 0.25
        fourth_tax = (taxable_income - 117450) * 0.28
        tax = first_tax + second_tax + third_tax + fourth_tax
        print(f'your tax for Head of Household is {tax:.2f}')

    elif taxable_income >= 190201 and taxable_income <= 372950:
        first_tax = 11950 * 0.10
        second_tax = (45500 - 11950) * 0.15
        third_tax = (117450 - 45500) * 0.25
        fourth_tax = (190200 - 117450) * 0.28
        fifth_tax = (taxable_income - 190200) * 0.33
        tax = first_tax + second_tax + third_tax + fourth_tax + fifth_tax
        print(f'your tax for Head of Household is {tax:.2f}')

    elif taxable_income >= 372951:
        first_tax = 11950 * 0.10
        second_tax = (45500 - 11950) * 0.15
        third_tax = (117450 - 45500) * 0.25
        fourth_tax = (190200 - 117450) * 0.28
        fifth_tax = (372950 - 190200) * 0.33
        sixth_tax = (taxable_income - 372950) * 0.35
        tax = first_tax + second_tax + third_tax + fourth_tax + fifth_tax + sixth_tax
        print(f'your tax for Head of Household is {tax:.2f}')
        
elif user_input > 3 or user_input < 0:
    print('Invalid input. There are 4 filing status. Enter 0 for single filers \n 1 for Married Filling Jointly \n 2 for Married filling separately \n 3 for Head of Household')
    
