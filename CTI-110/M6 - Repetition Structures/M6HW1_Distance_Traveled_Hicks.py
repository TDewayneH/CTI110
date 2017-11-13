
#CTI-110
#M6HW1 - Distance Traveled
#Terry Hicks
#13NOV17

def main():
    working = True
    while working:
        speed = int(input("What is the speed of teh vehicle in mph? "))
        hours = int(input("How many hours has it traveled? "))
        print("""
                    Hours\t Distance traveled
                    ________________________________

                """)
        for i in range(hours):
            distance = speed * (i + 1)
            if((i+1) <= 9):
                print("\t\t    ",i+1, "\t\t", distance)
            else:
                print("\t\t    ",i+1, "\t", distance)
        working = False

main()


input("\n\nPress enter to exit.")
