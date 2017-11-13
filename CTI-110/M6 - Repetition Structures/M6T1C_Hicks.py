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

"""
        Having a problem with this part of the code couldn't get it
        to do exactly what I wanted.. but I think what I ended up doing
        makes a pretty cool look so I am pushing it up to you guys.

        
def main():
    angle = 360 / numSides
    sides = range(numSides)
    distance = 80

    for i in sides:
        newFlake.forward(distance)
        newFlake.left(angle)
    #newFlake.left(90)
    for i in sides:
        branch()
"""    

def branch():
    for i in range(3):
        for i in range(3):
            newFlake.forward(40)            
            newFlake.backward(40)
            newFlake.right(45)
        newFlake.left(90)
        newFlake.backward(27)
        newFlake.left(45)
    newFlake.up()
    newFlake.right(180)
    newFlake.forward(80)
    newFlake.right(45)
    newFlake.backward(80)
    newFlake.left(90)
    newFlake.down()
    
    

for i in range(numSides):
    branch()
    
        
