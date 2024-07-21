def equal_strings(word1, word2):
    if len(word1) == len(word2):
        return True
 
    for length in range(len(word1)):
        if word1(length) == word2(length):
            return True

    return False

print(equal_strings('love', 'evol'))
