def only_floats(num1, num2):
    if type(num1) == float and type(num2) == float:
        return('2')
    elif type(num1) != float and type(num2) != float:
        return('0')
    else:
        return('1')    
print(only_floats(12.1, 23))
