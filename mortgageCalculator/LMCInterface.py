from __future__ import print_function

from LoanMortgageCalculator import LoanMortgageCalculator

import pylab as plt


def grab_loan_amount():
    return float(input("Loan amount (decimal): $"))


def grab_down_payment():
    return float(input("Down payment amount (decimal): $"))


def grab_annual_interest_rate():
    return float(input("Annual Interest Rate (%): "))


def grab_period_in_years():
    return int(input("Period/Number of years: "))

la = grab_loan_amount()
dp = grab_down_payment()
air = grab_annual_interest_rate()
piy = grab_period_in_years()

lmc = LoanMortgageCalculator(la, dp, air, piy)

print("Monthly payment = $", lmc.monthly_payment())

monthly_balances, monthly_interests, monthly_principals = lmc.generate_monthly_breakdowns()

i = 1
months = list()
for balance, principal, interest in zip(monthly_balances, monthly_principals, monthly_interests):
    months.append(i)
    print("After month ", i , " [balance = $", balance, " principal for month = $", principal, " interest for month = $", interest, "]")
    i += 1

fig1 = plt.figure()
plt.subplots_adjust(left=0.15, right=0.95, wspace=0.25, hspace=0.75)
plt.subplot(211)
plot1, = plt.plot(months, monthly_interests,'r')
plot2, = plt.plot(months, monthly_principals,'g')
plt.title('Mortgage amortization chart')
plt.xlabel('Months')
plt.ylabel('Monthly Payments')
plt.legend([plot1, plot2], ("Interest", "Principal"), numpoints=1)

plt.subplot(212)
plot3 = plt.plot(months, monthly_balances, 'b')
plt.title('Balance burn-down')
plt.xlabel('Months')
plt.ylabel('Loan Balance')

plt.show()
