for count in range(15):
    score = int(input(f'Enter score of student {count+1}: '))
    print('you entered', score)
    if score < 45:
        print('the student has failed this exam')
    else:
        print('the student has passed this exam')
