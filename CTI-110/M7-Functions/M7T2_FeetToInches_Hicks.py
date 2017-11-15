#A program to convert feet to inches
#15NOV17
#CTI-110 M7T2_FeetToInches
#Dewayne Hicks

def main():
    feet = int(input("Please enter the distance in feet: "))
    inches = show_inches(feet)
    print("The distance in inches is", inches)
    

def show_inches(feet):
    inches = feet * 12
    return inches

main()

input("\n\nPress enter to exit")
