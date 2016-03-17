# receive Input
initialBalance = float(raw_input("Enter your balance: "))
interestRate = float(raw_input("Enter your annual interest: "))

balance = initialBalance
monthlyInterestRate = interestRate / 12
lowerBoundPay = balance / 12
upperBoundPay = (balance * (1 + monthlyInterestRate) ** 12) / 12
