#CTI 110
#M6T1C - SnowFlake
#Dewayne Hicks
#13NOV17

import turtle
import random

snowFlake = turtle.Screen()
snowFlake.bgcolor("blue")
newFlake = turtle.Turtle()
newFlake.pencolor("black")
newFlake.pensize(5)

colors = ['green', 'white', 'red', 'purple', 'cyan', 'gold', 'yellow']
numSides = int(input("How many sides do you want it to have? "))
    
def main():
    angle = 360 / numSides
    sides = range(numSides)
    distance = 80

    for i in sides:
        newFlake.color('black')
        newFlake.forward(distance)
        branch()
        newFlake.left(angle) 

def branch():
    choice = random.randint(1,4)
    newFlake.color(random.choice(colors))
    if(choice == 1):
        for i in range(2):
            newFlake.forward(100)
            newFlake.right(60)
            newFlake.forward(100)
            newFlake.right(120)
    elif(choice == 2):
        for i in range(4):
            newFlake.forward(100)
            newFlake.right(90)
    elif(choice == 3):
        for i in range(2):
            newFlake.forward(100)
            newFlake.right(90)
            newFlake.forward(50)
            newFlake.right(90)
    else:
        for i in range(3):
            for i in range(3):
                newFlake.forward(30)
                newFlake.backward(30)
                newFlake.right(45)
            newFlake.left(90)
            newFlake.forward(30)
            newFlake.left(45)
        newFlake.right(45)
        newFlake.backward(90)
        newFlake.left(45)
main()
    
        
