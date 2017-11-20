#M5LAB
#Debugging
#Dewayne Hicks
#8NOV17

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

    
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F')

# program start
main()

input("\n\nPress enter to exit.")
