#CTI-110
#M6T2 - Bug Collector
#Dewayne Hicks
#13NOV17

def main():
    totalBugs = 0
    for i in range(7):
        bugsCollected = int(input("How many bugs did you collect today? "))
        totalBugs = bugsCollected + totalBugs
    print("You collected", totalBugs, "bugs this week!")

main()

input("\n\nPress enter to exit")
