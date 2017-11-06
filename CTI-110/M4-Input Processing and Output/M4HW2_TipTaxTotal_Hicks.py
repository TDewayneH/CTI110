#CTI-110
#M4HW2 - Tip Tax Total
#Dewayne Hicks
#6NOV17

print("""
        Tip, Tax, and Total calculator!
    """)


"""
    This code calculates all the cost
"""
foodCost = input("How much was your food? $")
tipAmmount = round(foodCost * .18,2)
salesTax = round(foodCost * .07,2)
totalCost = round(foodCost + tipAmmount + salesTax,2)


"""
    This code prints all the cost
"""
print("You should tip " + str(tipAmmount))
print("Your sales tax is " + str(salesTax))
print("Your total is " + str(totalCost))

#Just to keep it up until the user is done with the program
raw_input("\n\nPress enter to exit")
