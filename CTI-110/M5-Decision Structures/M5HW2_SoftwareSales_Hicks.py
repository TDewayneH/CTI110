#CTI-110
#M5HW2 - Software Sales
#Dewayne Hicks
#8NOV17

def main():
    print("""
          One prduct cost $99.
          
          If you buy in bulk you get a discount and it is as follows:
          
          Quantity 10-19:        10% discount          
          Quantity 20-49:        20% discount          
          Quantity 50-99:        30% discount
          Quantity 100+:         40% discount
          """)
    quantity = int(input("How many products would you like to buy? "))

    if(quantity < 10):
        print("You're price is ", quantity * 99)
    elif(quantity >= 10 and quantity < 20):
        print("You're price is ", (quantity * 99) / .10)
    elif(quantity >= 20 and quantity < 50):
        print("You're price is ", (quantity * 99) / .20)
    elif(quantity >= 50 and quantity < 100):
        print("You're price is ", (quantity * 99) / .30)
    else:
        print("You're price is ", (quantity * 99) / .40)
    
    
main()

input("\n\nPress enter to exit")
