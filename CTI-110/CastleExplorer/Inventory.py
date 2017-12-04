import CastleEx, colorama
colorama.init()
red = "\033[1;31m"
yellow = "\033[1;33m"
end = "\033[0;0m"

def openInventory(name, location, firstLoc, strength, gold, invtor, food,\
                  enemKilled, highScores):
#(gold,food,invtor=[]):
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
                if("Flaming Torch" not in invtor):
                    print("You bought a Flaming Torch")
                    gold -= 15
                    invtor.append("Flaming Torch")
                else:
                    print(yellow+"You alredy have a Flaming Torch"+end)
                
            else:
                print(red +"You don't have enough gold." + end)
                
        elif(choice == 2):
            if(gold>=10):
                if("Axe" not in invtor):
                    print("You bought an axe")
                    gold -= 10
                    invtor.append("Axe")
                else:
                    print(yellow + "You already have an Axe"+end)
                
            else:
                print(red+"You don't have enough gold."+end)
                
        elif(choice == 3):
            if(gold>=20):
                if("Sword" not in invtor):
                    print("You bought a sword")
                    gold -= 20
                    invtor.append("Sword")
                else:
                    print(yellow+"You already have a Sword"+end)
                
            else:
                print(red+"You don't have enough gold."+end)
                
        elif(choice == 4):
            choice2 = int(input("How much would you like to buy? "))
            if(gold>=choice2*2):
                print("You bought",choice2,"amouth of food for",choice2*2)
                gold -= choice2*2
                food += choice2
                
            else:
                print(red+"You don't have enough gold."+end)
                
        elif(choice == 5):
            if(gold>=30):
                if("Magic Amulet" not in invtor):
                    print("You bought a magic amulet")
                    gold -= 30
                    invtor.append("Magic Amulet")
                else:
                    print(yellow+"You already have the Magic Amulet"+end)
            else:
                print(red+"You don't have enough gold."+end)
                
        elif(choice == 6):
            if(gold>=50):
                if("Suit of Armor" not in invtor):
                    print("You bought a suit of armor")
                    gold -= 50
                    invtor.append("Suit of Armor")
                else:
                    print(yellow+"You already have a Suit of Armor"+end)
            else:
                print(red+"You don't have enough gold."+end)
                
        elif(choice == 0):
            CastleEx.takeAction(name, location, firstLoc, strength, gold,\
                                invtor, food, enemKilled, highScores)
