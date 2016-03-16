# Receive user input
balance = float(raw_input("Your balance: "))
annual_interest_rate = float(raw_input("Your annual interest rate: "))
monthly_payment_rate = float(raw_input("Your monthly payment rate: "))

# global variable, to save state
monthly_interest_rate = annual_interest_rate/12
total_amount_paid = 0

for month in range(1, 13):
	# Calculate the credit card
	min_monthly_payment = round(monthly_payment_rate * balance, 2)
	interest_paid = round(monthly_interest_rate * balance, 2)
	principal_paid = min_monthly_payment - interest_paid
	balance -= principal_paid
	total_amount_paid += min_monthly_payment

	# Display the result
	print "Month: ", month
	print "Minimum monthly payment: $", min_monthly_payment
	print "Remaining balance: $", balance

print "RESULT"
print "Total amount paid: $", total_amount_paid
print "Remaining balance: $", balance
