def biggest_odd(numbers_str):
    numbers = [int(number) for number in numbers_str.split()]
    
    biggest_odd = 0

    for number in numbers:
        if number % 2 != 0:
            if number == None or number > biggest_odd:
                biggest_odd = number
    return biggest_odd
    
print(biggest_odd("2 3 5 6 9"))
