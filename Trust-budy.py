#Trust Fund Buddy-Bad
# Demonstrates a logical error

print \
"""
Trust Fund Buddy

Totals your monthly spending so you don't have to
run out and get a JOB!

Please enter the requested, monthly costs. Since you are rich 
don't worry about the pennies just use dollar amounts only.

"""

car = int(raw_input("Porsche tune-ups: "))

rent = int(raw_input("Manhattan apartment: "))

jet = int(raw_input("Private Jet rentals: "))

gifts = int(raw_input("Gifts: "))

food = int(raw_input("Food Deliveries: "))

staff = int(raw_input("Staff (butler, chef, maid): "))

guru = int(raw_input("Gaming Guru: "))

gamefees = int(raw_input("total game fees per month: "))

total = (((((((car + rent) + jet) + gifts) + food) + staff) + guru) + gamefees) 

print "\nGrand Total " , total

raw_input("\nPress enter key to exit")
