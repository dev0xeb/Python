import string
from random import random


def generate_password(password):
    if len(password) < 8 or len(password) > 8:
        raise ValueError("Password must be at least 8 characters long")

    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    generated_password = ''
    generated_password += random.choice(upper_case)
    generated_password += random.choice(lower_case)
    generated_password += random.choice(symbols)
    generated_password += random.choice(numbers)
    generated_password += random.choice(lower_case)
    generated_password += random.choice(upper_case)
    generated_password += random.choice(symbols)
    generated_password += random.choice(numbers)

    upper_case_pattern = r'[A-Z]'
    lower_case_pattern = r'[a-z]'
    numbers_pattern = r'[0-9]'
    symbols_pattern = r'[\s]'


    return generated_password