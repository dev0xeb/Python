#recongnize what the input will be and put it as a parameter
#to store if the number is an even number or odd number intialize a variable called result
#check if the number is an even or odd number
#return the result

def even_or_odd(number):
    result = 0
    if number % 2 == 0:
        result = 'it is an even number'
    else:
        result = 'it is an odd number'
    return result
print(even_or_odd(5))
