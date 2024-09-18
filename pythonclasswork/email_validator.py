import re


def email_validator(email):
    pattern = r'^[a-z0-9@a-z.a-z]*'
    if re.fullmatch(pattern, email):
         return True
    return False
print(email_validator('clintonayomide98@gmail.com'))
