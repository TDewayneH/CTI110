#CTI-110
#M6T1B - Initials
#Dewayne Hicks
#13NOV17

import turtle

def main():
    fInitial = False
    lInitial = False

    while(fInitial == False):
        turtle.pensize(3)
        turtle.color("green")
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(50)
        turtle.right(180)
        turtle.forward(100)
        fInitial = True
        

    while(lInitial == False):
        turtle.pensize(5)
        turtle.color("blue")
        turtle.up()
        turtle.forward(100)
        turtle.down()
        turtle.left(-90)
        turtle.forward(100)
        turtle.left(180)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(180)
        turtle.forward(100)
        lInitial = True

main()

input("Press Enter to exit.")
