vowel = 0
consonant = 0
user_input = input('Enter your first name: ')
for character in user_input:
    print(character, end=' ')
    if character == 'a' or  character == 'A' or character == 'e'or  character == 'E' or character == 'i' or  character == 'I' or character == 'o' or character == 'O' or character == 'u' or  character == 'U':
        vowel+=1
    else:
        consonant+=1

print(f'there are {vowel} vowels and {consonant} consonant')
