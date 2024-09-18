def listortuple(number):
    list_number = number.split(',')
    number_tuple = tuple(list_number)
    list_number = str(list_number)
    number_tuple = str(number_tuple)
    new_number = list_number + number_tuple
    return new_number
print(listortuple("34,67,55,33,12,98"))

def listoftuple2(number):
    list_number = number.split(',')
    number_tuple = ()
    for num in list_number:
        number_tuple += (num,)
    list_number = str(list_number)
    number_tuple = str(number_tuple)
    new_number = list_number + number_tuple
    return new_number
print(listoftuple2("34,67,55,33,12,98"))



# number = input("Enter number")
# print(number)
# number_list = []
# number_tuple =()
# new_number = number.split(",")
# print(new_number)
# new_number = tuple(new_number)
# print(new_number)
