#CTI 110
#M6T1C - SnowFlake
#Dewayne Hicks
#13NOV17

import turtle

snowFlake = turtle.Screen()
newFlake = turtle.Turtle()

def main():
    for i in range(3):
        for i in range(3):
            newFlake.forward(30)
            newFlake.backward(30)
            newfalke.right(45)
        newFlake.left(90)
        newFlake.backward(30)
        newflake.left(45)
    
        
