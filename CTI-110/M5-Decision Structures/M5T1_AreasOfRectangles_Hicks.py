#M5T1_Hicks
#Areas of rectangles
#Dewayne Hicks
#8NOV17

def main():
    rect1Length = int(input("Please input the lenght of the first rectangle: "))
    rect1Width = int(input("Please input the widht of the first rectangle: "))

    rect2Lenght = int(input("Please input the lenght of the second rectangle: "))
    rect2Width = int(input("Please input the width of the second rectangle: "))


    rect1 = rect1Length*rect1Width
    rect2 = rect2Lenght*rect2Width

    if(rect1>rect2):
        print("The first rectangle has the greater area")
    elif(rect1<rect2):
        print("The second rectangle has the greater area")
    else:
        print("They have the same area")

main()


input("\n\nPress enter to exit")
