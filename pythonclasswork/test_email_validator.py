import unittest

import email_validator
class TestEmailValidator(unittest.TestCase):
    def test_valid_email(self):
        email_validator.email_validator('clintonayomide98@gmail.com')

    def test_if_email_isValid(self, ):
        expected = email_validator.email_validator('clintonayomide98@gmail.com')
        self.assertTrue(expected, True)