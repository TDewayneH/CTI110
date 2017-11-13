#CTI 110
#M6T1C - SnowFlake
#Dewayne Hicks
#13NOV17

import turtle

snowFlake = turtle.Screen()
snowFlake.bgcolor("blue")
newFlake = turtle.Turtle()
newFlake.pencolor("white")
newFlake.pensize(5)

numSides = 8
      
def main():
    angle = 360 / numSides
    sides = range(numSides)
    distance = 80

    for i in sides:
        newFlake.forward(distance)
        branch()
        newFlake.left(angle) 

def branch():
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
    
        
