from time import sleep
# Input from user
initialBalance = float(raw_input("Enter your balance: "))
interestRate = float(raw_input("Enter your annual interest rate: "))

# Initialize state
monthlyPayment = 0
monthlyInterestRate = interestRate / 12
balance = initialBalance
totalMonth = 0

while balance > 0:
    countMonth = 0
    balance = initialBalance
    monthlyPayment += 10 # in dollar $10, or you can use custom value $0.01

    while countMonth < 12 and balance > 0:
        countMonth += 1
        totalMonth += 1

        interest = monthlyInterestRate * balance
        balance -= monthlyPayment
        balance += interest
        print "Remaining balance: $", balance
        print "Month: ", countMonth
        # sleep(0.001)

balance = round(balance, 2)
print "RESULT"
print "Monthly Payment to pay (1 Year): $", monthlyPayment
print "Months needed: ", totalMonth
print "Your balance: $", balance
