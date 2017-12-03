#A game for the final project
#CTI-110
#Dewayne Hicks
#30NOV17
import re, sys, random, Monsters, Inventory, colorama
colorama.init()
green = "\033[1;32m"
red = "\033[1;31m"
yellow = "\033[1;33m"
end = "\033[0;0m"

#Set up for the game
gameMap = [
            [0, 2, 3, 0],
            [1, 0, 5, 0],
            [0, 4, 0, 1],
            [3, 5, 0, 0],
            [4, 0, 0, 2]
            ]
invtor = []
food = 0
def main():
    strength = 95
    gold = 50
    maxHP = 10
    HP = maxHP

    firstLoc = 0
    location = 0
    testingLoc = 0

    name = ''
    while name == '':
        temp = ''
        temp = input("What is your name adventurer? ")
        if not re.match("^[a-z]*$", temp.lower()):
            print(red + "Pleae only use letters" + end)
        else:
            name = temp

    print("Welcome",name,"Your current " + red + "strength " + end + "is"
          ,strength, "and you have",gold, yellow + "gold" + end + " on you.")

    firstLoc = gameMap[1]
    location = gameMap[0][1]
    takeAction(location, firstLoc, strength, gold, invtor, food)

def takeAction(location, firstLoc, strength, gold, invtor, food):
    canSee = False
    worth = 0
    print("You can type in Inventory to open your Inventory")
    while True:
        print("Your strength is",strength,"You have",gold,"gold on you")
            
        if(location == 1):
            print(green + "You are in the game room" + end)
        elif(location == 2):
            print(green + "You are currently in the Dinning room" + end)
        elif(location == 3):
            print(green + "You are currently in a bed room with a withered bed"\
                  " a rug with some stains on it. A broken table and some"\
                  " samshed pots." + end)
        elif(location == 4):
            print(green + "You are in libary"+end)
        elif(location == 5):
            print(green+"You are in the master bed room"+end)
          
        canNorth = False
        canSouth = False
        canEast = False
        canWest = False
        if(canSee):
            if(firstLoc[0] != 0):
                print("There is a door to the"+green+" North."+end)
                canNorth = True
            else:
                canNorth = False
            if(firstLoc[1] != 0):
                print("There is a path to the"+green+" South."+end)
                canSouth = True
            else:
                canSouth = False
            if(firstLoc[2] != 0):
                print("There is a open arch to the"+green+" East."+end)
                canEast = True
            else:
                canEast = False
            if(firstLoc[3] != 0):
                print("You can go"+green+" West"+end+" from here.")
                canWest = True
            else:
                canWest = False
        else:
            print("It is too dark to see anything...")

        move = input("What would you like to do? ")
        if("torch" in move.lower() or "light" in move.lower()):
            if("Flaming Torch" in invtor):
                print("You pull out your torch")
                canSee = True
            else:
                print(red + "You don't have anything to light up the area" + end)
        elif("quit" in move.lower()):
            print("You quit the game.")
            sys.exit()
        elif("eat" in move.lower() or "food" in move.lower()):
            if(food>0):
                print("You have",food,"food on you")
                choice = int(input("How much do you want to eat? "))
                if(food>=choice):
                    food-=choice
                    strength+=choice*5
                    print("You ate",choice,"food and recovered",choice*5\
                          ,"strength")
                else:
                    print(red + "You don't have enought food" + end)
            else:
                print(red +\
                      "You don't have any food open your invetory and buy some"\
                      +end)
        elif("north" in move.lower()):
            if(canNorth==True):
                if(location == 2):
                    if(strength>0):
                        firstLoc = gameMap[0]
                        location = 1
                        strength-=5
                        if(random.randint(1,4) == 2):
                            monsterInt = random.randint(1,4)
                            strength = Monsters.monster(\
                                monsterInt, strength, invtor)
                        elif(random.randint(1,4) == 4):
                            worth = random.randint(10, 100)
                            print("There is some treasure in the room"\
                                  " The treasure is worth",worth,\
                                  yellow + "gold"+ end +\
                                  " use pick up to get it")
                    else:
                       print("You have ran out of strength and died.")
                elif(location == 4):
                    if(strength>0):
                        firstLoc = gameMap[2]
                        location = 3
                        strength-=5
                        if(random.randint(1,4) == 2):
                            monsterInt = random.randint(1,4)
                            strength = Monsters.monster(\
                                monsterInt, strength, invtor)
                        elif(random.randint(1,4) == 4):
                            worth = random.randint(10, 100)
                            print("There is some treasure in the room"\
                                  " The treasure is worth",worth,\
                                  yellow + "gold"+ end +\
                                  " use pick up to get it")
                          
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 5):
                    if(strength>0):
                        firstLoc = gameMap[3]
                        location = 4
                        strength-=5
                        if(random.randint(1,4) == 2):
                            monsterInt = random.randint(1,4)
                            strength = Monsters.monster(\
                                monsterInt, strength, invtor)
                        elif(random.randint(1,4) == 4):
                            worth = random.randint(10, 100)
                            print("There is some treasure in the room"\
                                  " The treasure is worth",worth,\
                                  yellow + "gold"+ end +\
                                  " use pick up to get it")
                            
                    else:
                        print("You have ran out of strength and died.")
                else:
                    print("Shouldn't see this")
                           
            else:
                print("You cannot walk through walls")
        elif("south" in move.lower()):
            if(canSouth):
                if(location == 1):
                    if(strength>0):
                        firstLoc = gameMap[1]
                        location = 2
                        strength-=5
                        if(random.randint(1,4) == 2):
                            monsterInt = random.randint(1,4)
                            strength = Monsters.monster(\
                                monsterInt, strength, invtor)
                        elif(random.randint(1,4) == 4):
                            worth = random.randint(10, 100)
                            print("There is some treasure in the room"\
                                  " The treasure is worth",worth,\
                                  yellow + "gold"+ end +\
                                  " use pick up to get it")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 3):
                    if(strength>0):
                        firstLoc = gameMap[3]
                        location = 4
                        strength-=5
                        if(random.randint(1,4) == 2):
                            monsterInt = random.randint(1,4)
                            strength = Monsters.monster(\
                                monsterInt, strength, invtor)
                        elif(random.randint(1,4) == 4):
                            worth = random.randint(10, 100)
                            print("There is some treasure in the room"\
                                  " The treasure is worth",worth,\
                                  yellow + "gold"+ end +\
                                  " use pick up to get it")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 4):
                    if(strength>0):
                        firstLoc = gameMap[4]
                        location = 5
                        strength-=5
                        if(random.randint(1,4) == 2):
                            monsterInt = random.randint(1,4)
                            strength = Monsters.monster(\
                                monsterInt, strength, invtor)
                        elif(random.randint(1,4) == 4):
                            worth = random.randint(10, 100)
                            print("There is some treasure in the room"\
                                  " The treasure is worth",worth,\
                                  yellow + "gold"+ end +\
                                  " use pick up to get it")
                            
                    else:
                        print("You have ran out of strength and died.")
                else:
                    print("Shouldn't see this")
            else:
                print("You cannot walk through walls")
        elif("west" in move.lower()):
            if(canWest):
                if(location == 3):
                    if(strength>0):
                        firstLoc = gameMap[0]
                        location = 1
                        strength-=5
                        if(random.randint(1,4) == 2):
                            monsterInt = random.randint(1,4)
                            strength = Monsters.monster(\
                                monsterInt, strength, invtor)
                        elif(random.randint(1,4) == 4):
                            worth = random.randint(10, 100)
                            print("There is some treasure in the room"\
                                  " The treasure is worth",worth,\
                                  yellow + "gold"+ end +\
                                  " use pick up to get it")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 5):
                    if(strength>0):
                        firstLoc = gameMap[1]
                        location = 2
                        strength-=5
                        if(random.randint(1,4) == 2):
                            monsterInt = random.randint(1,4)
                            strength = Monsters.monster(\
                                monsterInt, strength, invtor)
                        elif(random.randint(1,4) == 4):
                            worth = random.randint(10, 100)
                            print("There is some treasure in the room"\
                                  " The treasure is worth",worth,\
                                  yellow + "gold"+ end +\
                                  " use pick up to get it")
                            
                    else:
                        print("You have ran out of strength and died.")
                else:
                    print("Shouldn't see this")
            else:
                print("You cannot walk through walls")
        elif("east" in move.lower()):
            if(canEast):
                if(location == 1):
                    if(strength>0):
                        firstLoc = gameMap[2]
                        location = 3
                        strength-=5
                        if(random.randint(1,4) == 2):
                            monsterInt = random.randint(1,4)
                            strength = Monsters.monster(\
                                monsterInt, strength, invtor)
                        elif(random.randint(1,4) == 4):
                            worth = random.randint(10, 100)
                            print("There is some treasure in the room"\
                                  " The treasure is worth",worth,\
                                  yellow + "gold"+ end +\
                                  " use pick up to get it")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 2):
                    if(strength>0):
                        firstLoc = gameMap[4]
                        location = 5
                        strength-=5
                        if(random.randint(1,4) == 2):
                            monsterInt = random.randint(1,4)
                            strength = Monsters.monster(\
                                monsterInt, strength, invtor)
                        elif(random.randint(1,4) == 4):
                            worth = random.randint(10, 100)
                            print("There is some treasure in the room"\
                                  " The treasure is worth",worth,\
                                  yellow + "gold"+ end +\
                                  " use pick up to get it")
                            
                    else:
                        print("You have ran out of strength and died.")
                else:
                    print("Shouldn't see this")
            else:
                print("You cannot walk through walls")
        elif("inventory" in move.lower() or "inv" in move.lower()):
            print("You are opening your Inv")
            Inventory.openInventory(location, firstLoc, strength, gold, invtor, food)
        elif("pick up" in move.lower()):
            if(worth!=0):
                print("You picked up the treasure and got",worth,"gold")
                gold += worth
            else:
                print("There isn't anything around worth taking")
        else:
            print("Invalid input please make another selection.")


    
main()
