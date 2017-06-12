import math


class LoanMortgageCalculator:
    def __init__(self, loan_amount, down_payment, annual_interest_rate, period_in_years):
        self.loan_amount = loan_amount
        self.down_payment = down_payment
        self.annual_interest_rate = annual_interest_rate
        self.period_in_years = period_in_years
        self.principal = self.loan_amount - self.down_payment
        self.number_of_monthly_periods = self.period_in_years * 12
        self.monthly_interest_rate = self.annual_interest_rate / 1200
        print("===================================================================")
        print("Created a LoanMortgageCalculator object with the following inputs: ")
        print("===================================================================")
        print("Loan Amount = $", self.loan_amount)
        print("Down Payment = $", self.down_payment)
        print("Annual Interest Rate = ", self.annual_interest_rate, "%")
        print("Period = ", self.period_in_years, " years")
        print("Number of months: ", self.number_of_monthly_periods)
        print("Principal: ", self.principal)
        print("===================================================================")

    def __calc_interest_mult(self, period):
        return math.pow((1 + self.monthly_interest_rate), period)

    def monthly_payment(self):
        return round(self.principal * (self.monthly_interest_rate * self.__calc_interest_mult(self.number_of_monthly_periods)) / (self.__calc_interest_mult(self.number_of_monthly_periods) - 1), 2)

    def generate_monthly_breakdowns(self):
        monthly_pay = self.monthly_payment()
        monthly_balances = list()
        monthly_principals = list()
        monthly_interests = list()
        i = 1
        while i <= self.number_of_monthly_periods:
            monthly_bal = round(self.calculate_monthly_balance(i), 2)
            monthly_balances.append(monthly_bal)
            monthly_int = round(monthly_bal * self.monthly_interest_rate, 2)
            monthly_interests.append(monthly_int)
            monthly_prin = round(monthly_pay - monthly_int, 2)
            monthly_principals.append(monthly_prin)
            i += 1
        return monthly_balances, monthly_interests, monthly_principals

    def calculate_monthly_balance(self, month):
        return self.principal * (self.__calc_interest_mult(self.number_of_monthly_periods) - self.__calc_interest_mult(month))/(self.__calc_interest_mult(self.number_of_monthly_periods) - 1)
