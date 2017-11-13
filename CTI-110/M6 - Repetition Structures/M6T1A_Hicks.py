#CTI-110
#M6T1A - Shapes
#Dewayne Hicks
#13NOV17

import turtle

def main():
    boxFinished = False
    recFinished = False

    while(boxFinished == False):
        for i in range(4):
            turtle.forward(50)
            turtle.left(90)
            boxFinished = True
        

    while(recFinished == False):
        turtle.up()
        turtle.forward(100)
        turtle.down()
        for i in range(2):
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            recFinished = True

main()

input("Press Enter to exit.")
