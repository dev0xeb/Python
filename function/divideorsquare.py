def divide_or_square(number):
    if number % 5 == 0:
        return number ** 0.5"{:.2f}"
    else:
        return number % 5
print(divide_or_square(10))
