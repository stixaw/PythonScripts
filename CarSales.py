#Car Sale program
# takes the base price of the car minus the downpayment
# adds the licensing fee,  processing fee, state tax 25% of base price,
# calculate monthly payments for 5 years

#get base price of Car
print """Welcome to the Car Sales program, this program allows you to 
prepare a car loan estimate based on the base sticker price of the car,
the down payment, the quoted interest rate and the number of years for the loan.
"""
base_price = int(raw_input("\nWhat is the base price of the car?(omit commas and dollar sign) $"))
down_payment = int(raw_input("\nWhat is your downpayment?(omit commas and dollar sign) $"))

try:
  term = int(raw_input("\nHow many years would you like to make payments? "))
except ValueError:
  print "please enter the number of years as a number"
  term = int(raw_input("\nHow many years would you like to make payments? "))
 
int_rate = float(raw_input("\nWhat is the quoted interest rate as a decimal value(ex:4%=.04)? "))

#figure Licensing Fee at 2% of base price
lic_fee = base_price * .05
print "Licensing Fee: %.2f" % lic_fee

#figure processing fee 1% of base price
proc_fee = base_price * .03
print "Processing fee: %.2f" % proc_fee

#State Sales Tax
sales_tax = base_price * .0925
print "State Sales Tax: %.2f" % sales_tax

#total cost of car with fees and taxes
total_price = ((((base_price - down_payment) + lic_fee) + proc_fee) + sales_tax)
print "\nGrand Total: $%.2f" % total_price

perc_int = int_rate * 100
num_pay = term * 12
month_int = int_rate / 12
comp_int = month_int + 1.0
Nth_power = comp_int ** num_pay
Monthly_payment = total_price*((month_int * Nth_power) / (Nth_power - 1))

print "\nYour estimated monthly payment for " ,term, "years, at a" ,perc_int,"%" + " would be $%.2f"% Monthly_payment



  
