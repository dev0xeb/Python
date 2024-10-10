class LoanCalculator:
    def __init__(self):
        self.borrower = None
        self.interest_rate:int = 24
        self.loan_amount = None
        self.loan_period:int = 1

    def set_borrower(self, borrower:str):
        self.borrower = borrower

    def get_borrower(self):
        return self.borrower



    def set_loan_amount(self, amount:int):
        if amount > 0:
            self.loan_amount = amount
        else:
            raise ValueError("Invalid Loan amount")
    def get_loan_amount(self):
        return self.loan_amount

    def get_loan_period(self):
        return self.loan_period

    def set_loan_period(self, loan_period:int):
        if loan_period != 1:
            raise ValueError("Invalid Loan period")
        else:
            self.loan_period = 1

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, interest_rate:int):
        if interest_rate != 24:
            raise ValueError("Invalid Interest Rate")
        else:
            self.interest_rate = 24

    def get_monthly_payment(self) -> float:
        monthly_rate = (self.interest_rate / 100)/ 12
        month_loan_period = self.loan_period * 12
        monthly_payment = (self.loan_amount * monthly_rate) / (1-(1 + monthly_rate)**-month_loan_period)
        return round(monthly_payment, 2)

    def get_total_loan_payment(self) -> float:
        monthly_payment = self.get_monthly_payment()
        total_loan_payment = self.loan_period * 12
        total_loan_payment *= monthly_payment
        return round(total_loan_payment, 2)