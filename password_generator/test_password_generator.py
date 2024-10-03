import unittest

import password_generator

class TestPassword(unittest.TestCase):
    def setUp(self):
        password_generator.generate_password()