def round_up_number(num):
    nearest_integer = round(num)
    nearest_tenths = round(num, 1)
    nearest_hundredths = round(num, 2)
    nearest_thousandths = round(num, 3)
    
    return nearest_hundredths

print(round_up_number(13.56449))
