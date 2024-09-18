def concatonate_2_strings(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    return new_str1 + " " +new_str2
print(concatonate_2_strings("Hello", "world"))

def add_ce_to_string(str1, ce):
    if len(str1) % 2 == 0:
        word_1, word_2 = str1[:len(str1) // 2], str1[len(str1) // 2:]
        return word_1 + ce + word_2
    return str1 + ce
# print(add_ce_to_string("Helloo", 'ce'))
# print(add_ce_to_string("Hello", 'ce'))

def number_of_occurence_in_a_tuple(word, character):
    character_list = list(character)
    character_count = word.count(character)
    character_list.append(str(character_count))
    character_list = tuple(character_list)
    return character_list

# print(number_of_occurence_in_a_tuple("Hello", 'l'))

def remove_special_character(word):
    replacement = ""
    for character in word:
        if character.isalpha():
            replacement += character
    return replacement

print(remove_special_character("he,ll.o"))