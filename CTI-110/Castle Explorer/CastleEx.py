#A game for the final project
#CTI-110
#Dewayne Hicks
#30NOV17
import re, sys, random

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
    strenght = 95
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
            print("Pleae only use letters")
        else:
            name = temp

    print("Welcome",name,"Your current strenght is",strenght,\
          "and you have",gold,"gold on you.")

    firstLoc = gameMap[1]
    location = gameMap[0][1]
    takeAction(location, firstLoc, strenght, gold, invtor, food)

def takeAction(location, firstLoc, strenght, gold, invtor, food):
    canSee = False
    monster = False
    worth = 0
    print("You can type in Inventory to open your Inventory")
    while True:
        if(monster):
            if(mosnterInt == 1):
                print("A zombie appears in front of you! Use Attack or Run")
                choice = input("What will you do?")
                if("attack" in choice.lower()):
                    if("Axe" in invtor):
                        print("You use your axe and cut the zombie down!")
                        monster = False
                    elif("Sword" in invtor):
                        if("Suit of Armor" in invtor):
                            print("You use your sword to attack the zombie"\
                              " But he tried to bite you but your armor"\
                              " saved you from it")
                            monster = False
                        elif("Magic Amulet"):
                            print("You use your sword to attack the zombie"\
                                  " But he was able to bite you your strenght"\
                                  " goes down 3. The amulet seems to have no effect"\
                                  " on the zombies")
                            strenght -= 3
                            monster = False
                        else:
                            print("You use your sword to attack the zombie"\
                                  " But he was able to bite you your strenght"\
                                  " goes down 3")
                            strenght -= 3
                            monster = False
                    else:
                        if("Suit of Armor" in invtor):
                            print("You have no weapon so you start to punch the"\
                                  " zombie but he gets a few bites in on you"\
                                  " before you kill him. Your armor saves you from damage")
                            monster = False
                        elif("Magic Amulet" in invtor):
                            print("You have no weapon so you start to punch the"\
                                  " zombie but he gets a few bites in on you"\
                                  " before you kill him. Your strenght goes down 5"\
                                  " The amulet seems to have no effect on the zombie")
                            strenght -= 5
                            monster = False
                        else:
                            print("You have no weapon so you start to punch the"\
                                  " zombie but he gets a few bites in on you"\
                                  " before you kill him. Your strenght goes down 5")
                            strenght -= 5
                            monster = False
                elif("run" in choice.lower()):
                    if(random.randint(1,2) == 2):
                        print("You escaped the monster")
                        monster = False
                else:
                    print("False input")
                
            elif(mosnterInt == 2):
                print("A wolf appears in front of you!")
                choice = input("What will you do?")
                if("attack" in choice.lower()):
                    if("Axe" in invtor):
                        print("You use your axe and cut the wolf down!")
                        monster = False
                    elif("Sword" in invtor):
                        if("Suit of Armor" in invtor):
                            print("You use your sword to attack the wolf"\
                                  " But he tried to bite you but your armor"\
                                  " saved you from it")
                            monster = False
                        elif("Magic Amult" in invtor):
                            print("You have no weapon so you start to punch the"\
                                  " zombie but he gets a few bites in on you"\
                                  " before you kill him. Your strenght goes down 3"\
                                  " The amult has no effect on the wolf")
                            strenght -= 3
                            monster = False
                        else:
                            if("Suit of Armor" in invtor):
                                print("You use your sword to attack the wolf"\
                                          " But he was able to bite you your strenght"\
                                          " Your armor saves you from any damage")
                                monster = False
                            elif("Magic Amult" in invtor):
                                print("You use your sword to attack the wolf"\
                                          " But he was able to bite you your strenght"\
                                          " goes down 3. The amult has no effect on the wolf")
                                strenght -= 3
                                monster = False
                            else:
                                print("You use your sword to attack the wolf"\
                                          " But he was able to bite you your strenght"\
                                          " goes down 3")
                                strenght -= 3
                                monster = False
                    else:
                        if("Suit of Armor" in invtor):
                            print("You have no weapon so you start to punch the"\
                                  " wolf but he gets a few bites in on you"\
                                  " before you kill him. Your armor saves you from damage")
                            monster = False
                        elif("Magic Amulet" in invtor):
                            print("You have no weapon so you start to punch the"\
                                      " wolf but he gets a few bites in on you"\
                                      " before you kill him. Your strenght goes down 5"\
                                      " The amult has no effect on the wolf")
                            strenght -= 5
                            monster = False
                        else:
                            print("You have no weapon so you start to punch the"\
                                      " wolf but he gets a few bites in on you"\
                                      " before you kill him. Your strenght goes down 5")
                            strenght -= 5
                            monster = False
                elif("run" in choice.lower()):
                    if(random.randint(1,2) == 2):
                        print("You escaped the monster")
                        monster = False
                else:
                    print("False input")
            elif(mosnterInt == 3):
                print("A dragon appears in front of you!")
                choice = input("What will you do?")
                if("attack" in choice.lower()):
                    if("Axe" in invtor):
                        if("Magic Amulet" in invtor):
                            print("You use your axe to attack the dragon!"\
                                      " He is very powher full but your amulet"\
                                      " saves you from any damage")
                            monster = False
                        elif("Suit of Armor" in invtor):
                            print("You use your axe to attack the dragon!"\
                                      " He is very powher full but your armor"\
                                      " saves you from some of the damage"\
                                      " you only lose 3 strenght")
                            strenght -= 3
                            monster = False
                        else:
                            print("You use your axe to attack the dragon!"\
                                      " He is very powher full and you lose"\
                                      " 10 strenght")
                            strenght -= 10
                            monster = False
                    elif("Sword" in invtor):
                        if("Magic Amulet" in invtor):
                            print("You use your sword to attack the dragon!"\
                                      " He is very powher full but your amulet"\
                                      " saves you from any damage")
                            monster = False
                        elif("Suit of Armor" in invtor):
                            print("You use your sword to attack the dragon!"\
                                      " He is very powher full but your armor"\
                                      " saves you from some of the damage"\
                                      " you only lose 5 strenght")
                            strenght -= 5
                            monster = False
                        else:
                            print("You use your sword to attack the dragon!"\
                                      " He is very powher full and you lose"\
                                      " 15 strenght")
                            strenght -= 15
                            monster = False
                    else:
                        if("Magic Amult" in invtor):
                                print("The amult let's you escape the dragon before you die")
                                monster = False
                        else:
                            print("You have no defense agains the dragon and it kills"\
                                      " you. Better luck next time")
                            sys.exit()
                elif("run" in choice.lower()):
                    print("The dragon is to smart for you to escape from")
                else:
                    print("False input")
            else:
                print("A slime monster appears in front of you!")
                choice = input("What will you do?")
                if("attack" in choice.lower()):
                    if("Axe" in invtor):
                        print("You use your axe to attack and kill the monster")
                        monster = False
                    elif("Sword" in invtor):
                        print("You use your sword to attack and kill the monster")
                        monster = False
                    else:
                        print("You begin to punch the slim killing it.")
                        monster = False
                elif("run" in choice.lower()):
                    print("You escaped the monster")
                    monster = False
                else:
                    print("False input")


                
        else:
            print("Your strenght is",strenght,"You have",gold,"gold on you")
            
            if(location == 1):
                print("You are in the game room")
            elif(location == 2):
                print("You are currently in the Dinning room")
            elif(location == 3):
                print("You are currently in a bed room with a withered bed"\
                      " a rug with some stains on it. A broken table and some"\
                      " samshed pots.")
            elif(location == 4):
                
                print("You are in libary")
            elif(location == 5):
                print("You are in the master bed room")
            
            canNorth = False
            canSouth = False
            canEast = False
            canWest = False
            if(canSee):
                if(firstLoc[0] != 0):
                    print("There is a door to the North.")
                    canNorth = True
                else:
                    canNorth = False
                if(firstLoc[1] != 0):
                    print("There is a path to the South.")
                    canSouth = True
                else:
                    canSouth = False
                if(firstLoc[2] != 0):
                    print("There is a open arch to the East.")
                    canEast = True
                else:
                    canEast = False
                if(firstLoc[3] != 0):
                    print("You can go West from here.")
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
                    print("You don't have anything to light up the area")
            elif("quit" in move.lower()):
                print("You quit the game.")
                sys.exit()
            elif("eat" in move.lower() or "food" in move.lower()):
                if(food>0):
                    print("You have",food,"food on you")
                    choice = int(input("How much do you want to eat? "))
                    if(food>choice):
                        food-=choice
                        strenght+=choice*5
                        print("You ate",choice,"food and recovered",choice*5\
                              ,"strenght")
                    else:
                        print("You don't have enought food")
                else:
                    print("You don't have any food open your invetory and buy some")
            elif(move.lower().startswith("n")):
                if(canNorth==True):
                    if(location == 2):
                        if(strenght>0):
                            firstLoc = gameMap[0]
                            location = 1
                            strenght-=5
                            if(random.randint(1,4) == 2):
                                monster = True
                                mosnterInt = random.randint(1,4)
                            elif(random.randint(1,4) == 4):
                                worth = random.randint(50, 300)
                                print("There is some treasure in the room"\
                                      "The treasure is worth",worth,"gold"\
                                      " use pick up to get it")
                        else:
                           print("You have ran out of strenght and died.")
                    elif(location == 4):
                        if(strenght>0):
                            firstLoc = gameMap[2]
                            location = 3
                            strenght-=5
                            if(random.randint(1,4) == 2):
                                monster = True
                                mosnterInt = random.randint(1,4)
                            elif(random.randint(1,4) == 4):
                                worth = random.randint(50, 300)
                                print("There is some treasure in the room"\
                                      "The treasure is worth",worth,"gold"\
                                      " use pick up to get it")
                            
                        else:
                            print("You have ran out of strenght and died.")
                    elif(location == 5):
                        if(strenght>0):
                            firstLoc = gameMap[3]
                            location = 4
                            strenght-=5
                            if(random.randint(1,4) == 2):
                                monster = True
                                mosnterInt = random.randint(1,4)
                            elif(random.randint(1,4) == 4):
                                worth = random.randint(50, 300)
                                print("There is some treasure in the room"\
                                      "The treasure is worth",worth,"gold"\
                                      " use pick up to get it")
                            
                        else:
                            print("You have ran out of strenght and died.")
                    else:
                        print("Shouldn't see this")
                            
                else:
                    print("You cannot walk through walls")
            elif(move.lower().startswith("s")):
                if(canSouth):
                    if(location == 1):
                        if(strenght>0):
                            firstLoc = gameMap[1]
                            location = 2
                            strenght-=5
                            if(random.randint(1,4) == 2):
                                monster = True
                                mosnterInt = random.randint(1,4)
                            elif(random.randint(1,4) == 4):
                                worth = random.randint(50, 300)
                                print("There is some treasure in the room"\
                                      "The treasure is worth",worth,"gold"\
                                      " use pick up to get it")
                            
                        else:
                            print("You have ran out of strenght and died.")
                    elif(location == 3):
                        if(strenght>0):
                            firstLoc = gameMap[3]
                            location = 4
                            strenght-=5
                            if(random.randint(1,4) == 2):
                                monster = True
                                mosnterInt = random.randint(1,4)
                            elif(random.randint(1,4) == 4):
                                worth = random.randint(50, 300)
                                print("There is some treasure in the room"\
                                      "The treasure is worth",worth,"gold"\
                                      " use pick up to get it")
                            
                        else:
                            print("You have ran out of strenght and died.")
                    elif(location == 4):
                        if(strenght>0):
                            firstLoc = gameMap[4]
                            location = 5
                            strenght-=5
                            if(random.randint(1,4) == 2):
                                monster = True
                                mosnterInt = random.randint(1,4)
                            elif(random.randint(1,4) == 4):
                                worth = random.randint(50, 300)
                                print("There is some treasure in the room"\
                                      "The treasure is worth",worth,"gold"\
                                      " use pick up to get it")
                            
                        else:
                            print("You have ran out of strenght and died.")
                    else:
                        print("Shouldn't see this")
                else:
                    print("You cannot walk through walls")
            elif(move.lower().startswith("w")):
                if(canWest):
                    if(location == 3):
                        if(strenght>0):
                            firstLoc = gameMap[0]
                            location = 1
                            strenght-=5
                            if(random.randint(1,4) == 2):
                                monster = True
                                mosnterInt = random.randint(1,4)
                            elif(random.randint(1,4) == 4):
                                worth = random.randint(50, 300)
                                print("There is some treasure in the room"\
                                      "The treasure is worth",worth,"gold"\
                                      " use pick up to get it")
                            
                        else:
                            print("You have ran out of strenght and died.")
                    elif(location == 5):
                        if(strenght>0):
                            firstLoc = gameMap[1]
                            location = 2
                            strenght-=5
                            if(random.randint(1,4) == 2):
                                monster = True
                                mosnterInt = random.randint(1,4)
                            elif(random.randint(1,4) == 4):
                                worth = random.randint(50, 300)
                                print("There is some treasure in the room"\
                                      "The treasure is worth",worth,"gold"\
                                      " use pick up to get it")
                            
                        else:
                            print("You have ran out of strenght and died.")
                    else:
                        print("Shouldn't see this")
                else:
                    print("You cannot walk through walls")
            elif(move.lower().startswith("e")):
                if(canEast):
                    if(location == 1):
                        if(strenght>0):
                            firstLoc = gameMap[2]
                            location = 3
                            strenght-=5
                            if(random.randint(1,4) == 2):
                                monster = True
                                mosnterInt = random.randint(1,4)
                            elif(random.randint(1,4) == 4):
                                worth = random.randint(50, 300)
                                print("There is some treasure in the room"\
                                      "The treasure is worth",worth,"gold"\
                                      " use pick up to get it")
                            
                        else:
                            print("You have ran out of strenght and died.")
                    elif(location == 2):
                        if(strenght>0):
                            firstLoc = gameMap[4]
                            location = 5
                            strenght-=5
                            if(random.randint(1,4) == 2):
                                monster = True
                                mosnterInt = random.randint(1,4)
                            elif(random.randint(1,4) == 4):
                                worth = random.randint(50, 300)
                                print("There is some treasure in the room"\
                                      "The treasure is worth",worth,"gold"\
                                      " use pick up to get it")
                            
                        else:
                            print("You have ran out of strenght and died.")
                    else:
                        print("Shouldn't see this")
                else:
                    print("You cannot walk through walls")
            elif(move.lower().startswith("i")):
                print("You are opening your Inv")
                openInventory(location,firstLoc,strenght, gold, invtor, food)
            elif("pick up" in move.lower()):
                if(worth!=0):
                    print("You picked up the treasure and got",worth,"gold")
                    gold += worth
                else:
                    print("There isn't anything around worth taking")
            else:
                print("Invalid input please make another selection.")

def openInventory(location, firstLoc, strenght, gold, invtor, food):
    while True:
        if(len(invtor)>0 and food>0):
            print("""
                    You have""",gold,"""gold on you.
                    You have""",invtor,"""item(s) in your inventory
                    You have""",food,"""amount of food.

                    YOU CAN BUY
                    1 - FLAMING TORCH ($15)
                    2 - AXE ($10)
                    3 - SWORD ($20)
                    4 - FOOD ($2 PER UNIT)
                    5 - MAGIC AMULET ($30)
                    6 - SUIT OF ARMOR ($50)
                    0 - TO CONTINUE ADVENTURE
                """)
        elif(len(invtor)>0 and food==0):
            print("""
                    You have""",gold,"""gold on you.
                    You have""",invtor,"""item(s) in your inventory

                    YOU CAN BUY
                    1 - FLAMING TORCH ($15)
                    2 - AXE ($10)
                    3 - SWORD ($20)
                    4 - FOOD ($2 PER UNIT)
                    5 - MAGIC AMULET ($30)
                    6 - SUIT OF ARMOR ($50)
                    0 - TO CONTINUE ADVENTURE
                """)
        elif(len(invtor)==0 and food>0):
            print("""
                    You have""",gold,"""gold on you.
                    You have""",food,"""amount of food.

                    YOU CAN BUY
                    1 - FLAMING TORCH ($15)
                    2 - AXE ($10)
                    3 - SWORD ($20)
                    4 - FOOD ($2 PER UNIT)
                    5 - MAGIC AMULET ($30)
                    6 - SUIT OF ARMOR ($50)
                    0 - TO CONTINUE ADVENTURE
                """)
        else:
             print("""
                    You have""",gold,"""gold on you.

                    YOU CAN BUY
                    1 - FLAMING TORCH ($15)
                    2 - AXE ($10)
                    3 - SWORD ($20)
                    4 - FOOD ($2 PER UNIT)
                    5 - MAGIC AMULET ($30)
                    6 - SUIT OF ARMOR ($50)
                    0 - TO CONTINUE ADVENTURE
                """)
        choice = int(input("Enter the number of item you want: "))
        if(choice == 1):
            if(gold>=15):
                print("You bought a Flaming Torch")
                gold -= 15
                invtor.append("Flaming Torch")
                
            else:
                print("You don't have enough gold.")
                
        elif(choice == 2):
            if(gold>=10):
                print("You bought an axe")
                gold -= 10
                invtor.append("Axe")
                
            else:
                print("You don't have enough gold.")
                
        elif(choice == 3):
            if(gold>=20):
                print("You bought a sword")
                gold -= 20
                invtor.append("Sword")
                
            else:
                print("You don't have enough gold.")
                
        elif(choice == 4):
            choice2 = int(input("How much would you like to buy? "))
            if(gold>=choice2*2):
                print("You bought",choice2,"amouth of food for",choice2*2)
                gold -= choice2*2
                food = choice2
                
            else:
                print("You don't have enough gold.")
                
        elif(choice == 5):
            if(gold>=30):
                print("You bought a magic amulet")
                gold -= 30
                invtor.append("Magic Amulet")
            else:
                print("You don't have enough gold.")
                
        elif(choice == 6):
            if(gold>=50):
                print("You bought a suit of armor")
                gold -= 50
                invtor.append("Suit of Armor")
            else:
                print("You don't have enough gold.")
                
        elif(choice == 0):
            takeAction(location, firstLoc, strenght, gold, invtor, food)
    
main()
