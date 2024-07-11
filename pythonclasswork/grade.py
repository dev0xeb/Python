score = int(input('Enter student score: '))

if score > 100:
    print ('invalid input')
    
if score >= 75 and score <= 100:
    print('A')

elif score >= 65 and score < 75:
    print ('B')

elif score >= 50 and score < 65:
    print ('C')

elif score >= 40 and score < 50:
    print ('D')

elif score >= 1 and score < 40:
    print ('F')


