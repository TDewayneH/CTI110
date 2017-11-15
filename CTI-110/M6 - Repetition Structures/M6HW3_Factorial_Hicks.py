#CTI-110
#M6HW3 - Factorial
#Terry Hicks
#13NOV17

def main():
    nonNegative = 0
    total = 0
    nonNegative = int(input("Enter a nonnegative integer: "))
    total = factorial(nonNegative)
    print("The factorial of", nonNegative, "is", total)

def factorial(number):
    num = 1
    while number != 1:
        num = num * number
        number = number - 1
    return num
        
    
"""
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)
"""        

main()


input("\n\nPress enter to exit.")

