def reverse(number):
    """Return the reversal of an integer"""
   



def is_palindrome(number):
    reversed_num = reverse(number)
    if reversed_num == number:
        return 'number is a palindrome'
    else:
        return 'number is not a palindrome'
    
print(is_palindrome(121))


def get_sorted(num1, num2, num3):
        number = [num1, num2, num3]
        number.sort()

        return number
print(get_sorted(3, 1, 2))
