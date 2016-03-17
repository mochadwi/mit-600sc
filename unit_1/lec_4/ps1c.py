# receive Input
initialBalance = float(raw_input("Enter your balance: "))
interestRate = float(raw_input("Enter your annual interest: "))

balance = initialBalance
monthlyInterestRate = interestRate / 12
lowerBoundPay = balance / 12
upperBoundPay = (balance * (1 + monthlyInterestRate) ** 12) / 12

while True:
    balance = initialBalance
    monthlyPayment = (lowerBoundPay + upperBoundPay) / 2 # bisection search

    for month in range(1,13):
        interest = round(balance * monthlyInterestRate, 2)
        balance += interest - monthlyPayment
        if balance <= 0:
            break

    if (upperBoundPay - lowerBoundPay < 0.005):
        # Print result
        print "RESULT"

        monthlyPayment = round(monthlyPayment + 0.004999, 2)
        print "Monthly Payment to pay (1 Year): $", round(monthlyPayment, 2)

        # recalculate
        balance = initialBalance
        for month in range(1,13):
            interest = round(balance * monthlyInterestRate, 2)
            balance += interest - monthlyPayment
            if balance <= 0:
                break

        print "Months needed: ", month
        print "Your balance: $", round(balance, 2)
        break
    elif balance < 0:
        # Paying too much
        upperBoundPay = monthlyPayment
    else:
        # Paying too little
        lowerBoundPay = monthlyPayment
