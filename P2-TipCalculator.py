print("Welcome to the tip calculator!\n")

#how much was bill amount?
bill_amount=float(input("What was the total bill? $"))
#how much was tip?
tip=int(input("How much tip would you like to give? 10, 12, or 15? " ))
#how many people ate?
no_people=int(input("How many people to split the bill? "))

#calculating the total money spent including the tip
total=bill_amount+((tip/100)*bill_amount)
print('Each person should pay: $'+str(total/no_people))