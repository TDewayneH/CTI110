#CTI-110
#M7T1 - Kilometer Converter
#Dewayne Hicks
#15NOV17

def main():
    kMiles = int(input("Please enter the distance in kilometers: "))
    miles = show_miles(kMiles)
    print("The distance in miles is", round(miles,2))
    

def show_miles(kMiles):
    miles = kMiles * .6214
    return miles

main()

input("\n\nPress enter to exit")
