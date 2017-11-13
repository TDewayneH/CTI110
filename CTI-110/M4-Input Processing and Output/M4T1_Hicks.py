#CTI-110
#M4T1 - Sales Prediction
#Dewayne Hicks
#1NOV17
#

"""
    This code takes the input from the user to calculate the profit
"""
totalSales = float(input("Please input the projected total sales: $"))
print(\
      """
        Calculating one moment please
      """)


"""
    This is the code to calculate the profit and print it for the user
"""
annualProfit = totalSales * 0.23
print('Your profit for the year is $' + str(annualProfit))


#Just to keep it up until the user is done with the program
input('\n\nPress ENTER to exit program.')
