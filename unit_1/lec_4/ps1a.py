# Declare a first initialization of variable
# min_monthly_payment = 0
# interest_paid = 0
# principal_paid = 0
# remaining_balance = 0
# total_amount_paid = 0

def paying_the_minimum(bal, ann_ir, mon_pr):
	# Calculate the credit card
	min_monthly_payment = mon_pr * bal
	interest_paid = ann_ir / 12 * bal
	principal_paid = min_monthly_payment - interest_paid
	remaining_balance = bal - principal_paid
	total_amount_paid = total_amount_paid + min_monthly_payment

	# For iterates each month
	for month in range(1, 13):
		# Display the result
		print "Month: " + str(month)
		print "Minimum monthly payment: $" + str(min_monthly_payment)
		print "Principle paid: $" + str(principal_paid)
		print "Remaining balance: $" + str(remaining_balance)

	print "RESULT"
	print "Total amount paid: $" + str(total_amount_paid)
	print "Remaining balance: $" + str(remaining_balance)

# Receive user input
balance = raw_input("Your balance: ")
annual_interest_rate = raw_input("Your annual interest rate: ")
monthly_payment_rate = raw_input("Your monthly payment rate: ")

# Run the function
paying_the_minimum(float(balance), float(annual_interest_rate), float(monthly_payment_rate));
