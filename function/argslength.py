def get_length(string):
    string_length = 0
    for letters in string:
        string_length+=1
    return string_length
print(get_length('love'))
print(get_length('11'))
print(get_length([1,2,3,4,5]))
