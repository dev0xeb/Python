import unittest
from loan_app.loan_calculator import LoanCalculator

class TestLoanCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = LoanCalculator()

    def test_intilization(self):
        self.assertIsNone(self.calculator.get_borrower())
        self.assertEqual(self.calculator.get_interest_rate(), 24)
        self.assertIsNone(self.calculator.get_loan_amount())
        self.assertEqual(self.calculator.get_loan_period(), 1)

    def test_set_borrower(self):
        self.calculator.set_borrower("Ayoade Clinton")
        self.assertEqual(self.calculator.get_borrower(), "Ayoade Clinton")

    def test_set_interest_rate(self):
        self.calculator.set_borrower("Ayoade Clinton")
        self.calculator.set_loan_amount(4000)
        self.assertEqual(self.calculator.get_loan_amount(), 4000)

    def test_set_loan_period(self):
        self.calculator.set_borrower("Ayoade Clinton")
        self.calculator.set_loan_amount(4000)
        self.assertEqual(self.calculator.get_loan_amount(), 4000)
        self.assertEqual(self.calculator.get_loan_period(), 1)

    def test_monthly_payment(self):
        self.calculator.set_borrower("Ayoade Clinton")
        self.calculator.set_loan_amount(4000)
        self.assertEqual(self.calculator.get_interest_rate(), 24)
        self.assertEqual(self.calculator.get_loan_period(), 1)
        self.assertEqual(self.calculator.get_monthly_payment(), 378.24)

    def test_total_loan_payment(self):
        self.calculator.set_borrower("Ayoade Clinton")
        self.calculator.set_loan_amount(10000)
        self.assertEqual(self.calculator.get_interest_rate(), 24)
        self.assertEqual(self.calculator.get_loan_period(), 1)
        self.assertEqual(self.calculator.get_total_loan_payment(), 11347.20)

    def test_invalid_loan_amount(self):
        self.calculator.set_borrower("Ayoade Clinton")
        self.assertRaises(ValueError, self.calculator.set_loan_amount, -4000)

    def test_interest_rate_cannot_change(self):
        self.calculator.set_borrower("Ayoade Clinton")
        self.calculator.set_loan_amount(4000)
        self.assertRaises(ValueError, self.calculator.set_interest_rate, 1)

    def test_loan_period_cannot_change(self):
        self.calculator.set_borrower("Ayoade Clinton")
        self.calculator.set_loan_amount(4000)
        self.calculator.get_interest_rate()
        self.assertRaises(ValueError, self.calculator.set_loan_period, 24)

    def test_for_float_loan_amount(self):
        self.calculator.set_borrower("Ayoade Clinton")
        self.calculator.set_loan_amount(4000.50)
        self.calculator.get_interest_rate()
        self.calculator.get_loan_period()
        self.assertEqual(self.calculator.get_loan_amount(), 4000.50)