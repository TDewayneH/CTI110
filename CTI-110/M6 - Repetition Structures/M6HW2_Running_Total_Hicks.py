#CTI-110
#M6HW2 - Running Total
#Terry Hicks
#13NOV17

def main():
    grade = 0
    total = 0
    while grade >= 0:
        grade = int(input("Enter a number: "))
        if grade >= 0:
            total = grade + total
    print("Total:", total)
        

main()


input("\n\nPress enter to exit.")
