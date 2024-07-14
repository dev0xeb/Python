
user_ans1 = input('What is your problem: ')

user_ans2 = int(input('Have you had this problem before. Enter 1 for yes and 0 for NO: '))
if user_ans2 == 1:
    print('Well, you have it again')
elif user_ans2 == 0:
    print('Well, you have it now')
else:
    print('Invalid input, Try again')
