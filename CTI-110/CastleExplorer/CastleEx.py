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
            [0, 2, 3, 0, 0, 0],#1
            [1, 0, 5, 0, 0, 0],#2
            [0, 4, 0, 1, 6, 0],#3
            [3, 5, 0, 0, 0, 10],#4
            [4, 0, 0, 2, 0, 0],#5
            [0, 0, 0, 0, 0, 0],#6
            [0, 0, 8, 0, 0, 6],#7
            [0, 9, 0, 7, 0, 0],#8
            [8, 0, 0, 0, 0, 0],#9
            [0, 0, 0, 0, 0, 0],#10
            [0, 0, 12, 0, 10, 0],#11
            [0, 13, 0, 11, 0, 0],#12
            [12, 0, 0, 14, 0, 0],#13
            [0, 0, 0, 0, 0, 0],#14
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
    fightDragon = True
    print("You can type in Inventory to open your Inventory")
    while True:
        print("Your strength is",strength,"You have",gold,"gold on you")
            
        if(location == 1):
            print(green + "You are in the game room. You see a pool table"\
                  " the billards are there but you can't find any pool sticks."\
                  " There is also some dart bords and a few tables to play"\
                  " cards on."+ end)
        elif(location == 2):
            print(green + "You are currently in the Dinning room."\
                  " There is a huge table where some plates are still out."\
                  " It looks like they were in the middle of setting up."+ end)
        elif(location == 3):
            print(green + "You are currently in a bed room with a withered bed"\
                  " a rug with some stains on it. A broken table and some"\
                  " samshed pots."\
                  " \nYou can take the stairs it is a grand stair case."+ end)
        elif(location == 4):
            print(green + "You are in the libary."\
                  " There are what appears to be a million books on shelves"\
                  " that appear to reach to the heavens."\
                  " \nYou find a small lift wich you can use to go between"\
                  " the basment and ground floor."+end)
        elif(location == 5):
            print(green+"You are in the master bed room. The bed is so big"\
                  " you could easily fit 20 people on it. There is a nice"\
                  " fire place and a changing area that looks like"\
                  " it was recently used."+end)
        elif(location == 6):
            print(green+"You take the stairs it is a grand stair case."+end)
        elif(location == 7):
            print(green+"You are in what appears to be a maids chamber."\
                  " After looking around a bit you realize there isn't much"\
                  " in this room."\
                  " \nYou can take the stairs it is a grand stair case."+end)
        elif(location == 8):
            print(green+"This room appears to be the dinning area for the"\
                  " staff. Again there really isn't much in this room but"\
                  " it does appear to be very clean considering."+end)
        elif(location == 9):
            print(green+"This appears to be the room for the master butler."\
                  " His room is very tidy and neat. Strange how this room"\
                  " appears to be unaffected by the amount of time it's been"\
                  " unoccupied."+end)
        elif(location == 10):
            print(green+"You find a small lift wich you can use to go between"\
                  " the basment and ground floor."+end)
        elif(location == 11):
            print(green+"You are in the basment floor where it looks like the"\
                  " maids do the laundry. There are a few tubs full of water."\
                  " It looks like the water was recently poured."\
                  " \nYou find a small lift wich you can use to go between"\
                  " the basment and ground floor."+end)
        elif(location == 12):
            print(green+"You are in the room where they stored the food"\
                  " and wine, it looks like the wine is well perserved."\
                  " I bet it is aged amazingly."+end)
        elif(location == 13):
            print(green+"You are in a room that doesn't look like it"\
                  " was orginally part of the castle. It looks like someone"\
                  " was down here diggin to get into the castle.. or maybe"\
                  " get out?"+end)
        elif(location == 14):
            print(green+"You have exited the castle. Congulations on getting"\
                  " out of the castle with your life!"+end)
          
        canNorth = False
        canSouth = False
        canEast = False
        canWest = False
        canUp = False
        canDown = False
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
            if(firstLoc[4] != 0):
                if(location == 3):
                    print("You can go"+green+" Up stairs"+end+" from here.")
                    canUp = True
                else:
                    print("You can go"+green+" Up the lift"+end+" from here.")
                    canUp = True
            else:
                canUp = False
            if(firstLoc[5] != 0):
                if(location == 7):
                    print("You can go"+green+" Down stairs"+end+" from here.")
                    canDown = True
                else:
                    print("You can go"+green+" Down the lift"+end+" from here.")
                    canDown = True
            else:
                canDown = False
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
        elif("wine" in move.lower()):
            if(location == 12):
                print("You check the wine you are tempted to take a bottle"\
                      " but you have a feeling someone is watching you so"\
                      " you place it back down.")
            else:
                print("What wine?")
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
                                  " use get to pick it up.")
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
                                  " use get to pick it up.")
                          
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
                                  " use get to pick it up.")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 9):
                    if(strength>0):
                        firstLoc = gameMap[7]
                        location = 8
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
                                  " use get to pick it up.")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 13):
                    if(strength>0):
                        firstLoc = gameMap[11]
                        location = 12
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
                                  " use get to pick it up.")
                            
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
                                  " use get to pick it up.")
                            
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
                                  " use get to pick it up.")
                            
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
                                  " use get to pick it up.")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 8):
                    if(strength>0):
                        firstLoc = gameMap[8]
                        location = 9
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
                                  " use get to pick it up.")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 12):
                    if(strength>0):
                        firstLoc = gameMap[12]
                        location = 13
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
                                  " use get to pick it up.")
                            
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
                                  " use get to pick it up.")
                            
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
                                  " use get to pick it up.")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 8):
                    if(strength>0):
                        firstLoc = gameMap[6]
                        location = 7
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
                                  " use get to pick it up.")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 12):
                    if(strength>0):
                        firstLoc = gameMap[10]
                        location = 11
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
                                  " use get to pick it up.")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 13):
                    if(strength>0):
                        if(fightDragon):
                            strength = Monsters.monster(\
                                5, strength, invtor)
                            fightDragon = False
                        else:
                            firstLoc = gameMap[13]
                            location = 14
                            sys.exit()
                            
                            
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
                                  " use get to pick it up.")
                            
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
                                  " use get to pick it up.")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 7):
                    if(strength>0):
                        firstLoc = gameMap[7]
                        location = 8
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
                                  " use get to pick it up.")
                            
                    else:
                        print("You have ran out of strength and died.")
                elif(location == 11):
                    if(strength>0):
                        firstLoc = gameMap[11]
                        location = 12
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
                                  " use get to pick it up.")
                            
                    else:
                        print("You have ran out of strength and died.")
                else:
                    print("Shouldn't see this")
            else:
                print("You cannot walk through walls")
        elif("up" in move.lower()):
            if(canUp):
                if(location == 3):
                        if(strength>0):
                            firstLoc = gameMap[6]
                            location = 7
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
                                      " use get to pick it up.")
                        else:
                            print("You have ran out of strength and died.")
                elif(location == 11):
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
                                      " use get to pick it up.")
                                
                        else:
                            print("You have ran out of strength and died.")
                else:
                    print("You shouldn't see this.")
            else:
                print("You can phase through the roof.")
        elif("down" in move.lower()):
            if(canDown):
                if(location == 7):
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
                                      " use get to pick it up.")
                        else:
                            print("You have ran out of strength and died.")
                elif(location == 4):
                        if(strength>0):
                            firstLoc = gameMap[10]
                            location = 11
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
                                      " use get to pick it up.")
                                
                        else:
                            print("You have ran out of strength and died.")
                else:
                    print("You shouldn't see this.")
            else:
                print("You can get through the floor.")
        
        elif("inventory" in move.lower() or "inv" in move.lower()):
            print("You are opening your Inv")
            Inventory.openInventory(location, firstLoc, strength, gold, invtor, food)
        elif("get" in move.lower()):
            if(worth!=0):
                print("You picked up the treasure and got",worth,"gold")
                gold += worth
            else:
                print("There isn't anything around worth taking")
        else:
            print("Invalid input please make another selection.")


    
main()

input("Press enter to exit.")
