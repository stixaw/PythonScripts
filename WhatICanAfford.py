# Price of a Car i can afford progrm
#this is  program helps you to determine the general price of a car based on the years of a loan and the payment you want to make.

print"""
This program helps someone going to buy a car,  by asking for the number of years they would like to pay, the
monthly payment they can afford and the downpayment they can make on the car.
It is an estimate based on 8% in fees of the total cost of the car and 9.25% sales tax.
"""

#How many years do you want to pay for this car?
term = int(raw_input("\nHow many years would you like to make payments? "))

#how much can you afford for a monthly payment?
monthly_payment = float(raw_input("\nHow much can you afford to pay each month(in dollars and cents)? $"))

#how much down payment
down_payment = float(raw_input("\nHow much can you afford for a down payment(omit commas and dollar sign)? $"))

#interest rate you are offered
int_rate = float(raw_input("\nWhat is the estimated interest rate as a decimal value(ex:4%=.04)? "))

#Find Total Price
num_pay = term * 12
month_int = int_rate / 12
comp_int = month_int + 1.0
Nth_power = comp_int ** num_pay
total_price = monthly_payment / ((month_int * Nth_power) / (Nth_power - 1))
round_total = round(total_price, 2)

#original price
base1 = round_total + down_payment

#original processing fees
base2 = round(base1 * .08, 2)

#original sales tax
base3 = round(base1 * .0925, 2)

base_price = (base1 - (base2 + base3)) + 400

print "Based on the data you provided, the Base Sticker price you should look for is:"+ "$" +" %.2f"% base_price

raw_input("\nPress Enter to Exit!")