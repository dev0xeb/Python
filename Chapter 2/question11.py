userinput = int(input("Enter a five digit number: "))

fifth_num = int (userinput % 10)
fourth_num = int ((userinput / 10) %10)
third_num = int ((userinput / 100) % 10)
second_num = int ((userinput / 1000)% 10)
first_num = int(userinput / 10000)

separate_num = (first_num,   second_num,   third_num,   fourth_num,   fifth_num)
print(separate_num)
