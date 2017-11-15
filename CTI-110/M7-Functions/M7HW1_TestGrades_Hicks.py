#A program to show the average test scores and give a grade
#15NOV17
#CTI-110 M7HW1 Test Average and Grade
#Dewayne Hicks

def main():
    totalTest = getGrade()
    grade = giveGrade(totalTest)
    print("You average of your test is", totalTest, ". Which gives you a"\
          " grade score of", grade)
    
    

def getGrade():
    grade = 0
    total = 0
    number = 0
    while grade >= 0:
        grade = int(input("Enter your test score (one at a time enter "\
                          "a neagtive number to exit): "))
        if grade >= 0:
            total = grade + total
            number += 1
    return total / number

def giveGrade(totalTest):
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50

    if totalTest >= A_score:
        return "A"
    elif totalTest < A_score and totalTest >= B_score:
        return "B"
    elif totalTest < B_score and totalTest >= C_score:
        return "C"
    elif totalTest < C_score and totalTest >= D_score:
        return "D"
    else:
        return "F"
    

main()

input("\n\nPress enter to exit")
