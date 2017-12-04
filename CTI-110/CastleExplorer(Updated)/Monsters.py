import colorama, random, sys
colorama.init()

def monster(monsterInt, strength, enemKilled, invtor=[]):
    red = "\033[1;31m"
    blue = "\033[1;34m"
    end = "\033[0;0m"
    monsterLive = True
    while monsterLive:
        if(monsterInt == 1):
            print(red + "A zombie appears in front of you!" + end\
                  + " Use Attack or Run")
            choice = input("What will you do? ")
            if("attack" in choice.lower()):
                if("Axe" in invtor):
                    print("You use your axe and cut the zombie down!")
                    monsterLive = False
                elif("Sword" in invtor):
                    if("Suit of Armor" in invtor):
                        print("You use your sword to attack the zombie"\
                            " But he tried to bite you but your armor"\
                            " saved you from it")
                        enemKilled += 1
                        monsterLive = False
                    elif("Magic Amulet"):
                        print("You use your sword to attack the zombie"\
                              " But he was able to bite you." + red +\
                              " Your strength goes down 3. The amulet seems to"\
                              " have no effect on the zombies." + end)
                        strength -= 3
                        enemKilled += 1
                        monsterLive = False
                    else:
                        print("You use your sword to attack the zombie"\
                              " But he was able to bite you." + red +\
                              " your strength goes down 3" + end)
                        strength -= 3
                        enemKilled += 1
                        monsterLive = False
                else:
                    if("Suit of Armor" in invtor):
                        print("You have no weapon so you start to punch the"\
                              " zombie but he gets a few bites in on you"\
                              " before you kill him. Your armor saves you from damage")
                        enemKilled += 1
                        monsterLive = False
                    elif("Magic Amulet" in invtor):
                        print("You have no weapon so you start to punch the"\
                              " zombie but he gets a few bites in on you"\
                              " before you kill him." + red +\
                              " Your strength goes down 5. The amulet seems"\
                              " to have no effect on the zombie" + end)
                        strength -= 5
                        enemKilled += 1
                        monsterLive = False
                    else:
                        print("You have no weapon so you start to punch the"\
                              " zombie but he gets a few bites in on you"\
                              " before you kill him." + red +\
                              " Your strength goes down 5" + end)
                        strength -= 5
                        enemKilled += 1
                        monsterLive = False
            elif("run" in choice.lower()):
                if(random.randint(1,2) == 2):
                    print("You escaped the monster")
                    monsterLive = False
                else:
                    print(red+"You faild to escape"+end)
                    monster(monsterInt,strength,enemKilled,invtor)
            else:
                print("False input")
                monster(monsterInt,strength,enemKilled,invtor)
                    
        elif(monsterInt == 2):
            print(red + "A wolf appears in front of you!" + end +\
                  " Use Attack or run.")
            choice = input("What will you do? ")
            if("attack" in choice.lower()):
                if("Axe" in invtor):
                    print("You use your axe and cut the wolf down!")
                    enemKilled += 1
                    monsterLive = False
                elif("Sword" in invtor):
                    if("Suit of Armor" in invtor):
                        print("You use your sword to attack the wolf"\
                              " But he tried to bite you but your armor"\
                              " saved you from it")
                        enemKilled += 1
                        monsterLive = False
                    elif("Magic Amult" in invtor):
                        print("You have no weapon so you start to punch the"\
                              " zombie but he gets a few bites in on you"\
                              " before you kill him." + red +\
                              " Your strength goes down 3 The amult has"\
                              " no effect on the wolf" + end)
                        strength -= 3
                        enemKilled += 1
                        monsterLive = False
                    else:
                        print("You use your sword to attack the wolf"\
                              " But he was able to bite you."\
                              " Your strength goes down 3."+end)
                        strength -= 3
                        enemKilled += 1
                        monsterLive = False
                else:
                    if("Suit of Armor" in invtor):
                        print("You have no weapon so you start to punch the"\
                              " wolf but he gets a few bites in on you"\
                              " before you kill him. Your armor saves you from damage")
                        enemKilled += 1
                        monsterLive = False
                    elif("Magic Amulet" in invtor):
                        print("You have no weapon so you start to punch the"\
                              " wolf but he gets a few bites in on you"\
                              " before you kill him." + red +\
                              " Your strength goes down 5"\
                              " The amult has no effect on the wolf" + red)
                        strength -= 5
                        enemKilled += 1
                        monsterLive = False
                    else:
                        print("You have no weapon so you start to punch the"\
                              " wolf but he gets a few bites in on you"\
                              " before you kill him." + red +\
                              " Your strength goes down 5" + end)
                        strength -= 5
                        enemKilled += 1
                        monsterLive = False
            elif("run" in choice.lower()):
                if(random.randint(1,2) == 2):
                    print("You escaped the monster")
                    monsterLive = False
                else:
                    print(red+"You faild to escape"+end)
                    monster(monsterInt,strength,enemKilled,invtor)
            else:
                print("False input")
                monster(monsterInt,strength,enemKilled,invtor)
        
        elif(monsterInt == 3):
            print(blue + "A Vampire appears in front of you!" + end +\
                  " Use Attack or Run.")
            choice = input("What will you do? ")
            if("attack" in choice.lower()):
                if("Axe" in invtor):
                    if("Magic Amulet" in invtor):
                        print("You use your axe to attack the Vampire!"\
                              " He is powerful but your amulet"\
                              " saves you from any damage")
                        enemKilled += 1
                        monsterLive = False
                    elif("Suit of Armor" in invtor):
                        print("You use your axe to attack the Vampire!"\
                              " He is powerful but your armor"\
                              " saves you from some of the damage"\
                              + red +" you only lose 3 strength"+end)
                        strength -= 3
                        enemKilled += 1
                        monsterLive = False
                    else:
                        print("You use your axe to attack the Vampire!"\
                              " He is powerful." + red + " You lose"\
                              " 10 strength"+end)
                        strength -= 5
                        enemKilled += 1
                        monsterLive = False
                elif("Sword" in invtor):
                    if("Magic Amulet" in invtor):
                        print("You use your sword to attack the Vampire!"\
                              " He is powerful but your amulet"\
                              " saves you from any damage")
                        enemKilled += 1
                        monsterLive = False
                    elif("Suit of Armor" in invtor):
                        print("You use your sword to attack the Vampire!"\
                              " He is powerful but your armor"\
                              " saves you from some of the damage"\
                              + red +" you only lose 5 strength"+end)
                        strength -= 5
                        enemKilled += 1
                        monsterLive = False
                    else:
                        print("You use your sword to attack the Vampire!"\
                              " He is powerful." + red +" You lose"\
                              " 10 strength")
                        strength -= 10
                        enemKilled += 1
                        monsterLive = False
                else:
                    if("Magic Amulet" in invtor):
                        print("You have no items to fight the Vampire."\
                              " He is powerful but your amulet"\
                              " let's you escape")
                        monsterLive = False
                    elif("Suit of Armor" in invtor):
                        print("You use your fist to attack the Vampire!"\
                              " He is powerful but your armor"\
                              " saves you from some of the damage"\
                              + red +" you lose 15 strength"+end)
                        strength -= 15
                        enemKilled += 1
                        monsterLive = False
                    else:
                        print("You have no defense or weapons to fight"\
                              " You throw yourself at the vampire punching"\
                              " and kicking."+red+" You lose 30 strength."+end)
                        strength -= 30
                        enemKilled += 1
                        monsterLive = False
            elif("run" in choice.lower()):
                if(random.randint(1,2) == 2):
                    print("You escaped the monster")
                    monsterLive = False
                else:
                    print(red+"You faild to escape"+end)
                    monster(monsterInt,strength,enemKilled,invtor)
            else:
                print("False input")
                monster(monsterInt,strength,enemKilled,invtor)
        elif(monsterInt == 5):
            print(blue + "A dragon appears in front of you!" + end +\
                  " You can't run from this powerful enemy")
            choice = input("What will you do? ")
            if("attack" in choice.lower()):
                if("Axe" in invtor):
                    if("Magic Amulet" in invtor):
                        print("You use your axe to attack the dragon!"\
                              " He is very powerful but your amulet"\
                              " saves you from any damage")
                        monsterLive = False
                    elif("Suit of Armor" in invtor):
                        print("You use your axe to attack the dragon!"\
                              " He is very powerful but your armor"\
                              " saves you from some of the damage"\
                              + red +" you only lose 3 strength"+end)
                        strength -= 3
                        enemKilled += 1
                        monsterLive = False
                    else:
                        print("You use your axe to attack the dragon!"\
                              " He is very powerful." + red + " You lose"\
                              " 10 strength"+end)
                        strength -= 10
                        enemKilled += 1
                        monsterLive = False
                elif("Sword" in invtor):
                    if("Magic Amulet" in invtor):
                        print("You use your sword to attack the dragon!"\
                              " He is very powher full but your amulet"\
                              " saves you from any damage")
                        monsterLive = False
                    elif("Suit of Armor" in invtor):
                        print("You use your sword to attack the dragon!"\
                              " He is very powerful but your armor"\
                              " saves you from some of the damage"\
                              + red +" you only lose 5 strength"+end)
                        strength -= 5
                        enemKilled += 1
                        monsterLive = False
                    else:
                        print("You use your sword to attack the dragon!"\
                              " He is very powerful." + red +" You lose"\
                              " 15 strength")
                        strength -= 15
                        enemKilled += 1
                        monsterLive = False
                else:
                    if("Magic Amult" in invtor):
                        print("The amult let's you escape the dragon"\
                              " before you die. You might want to go find"\
                              " something to help you fight the dragon."\
                              " Probably something"+ red + " magical.."+end)
                        monsterLive = False
                    else:
                        print(red + "You have no defense agains the dragon and it kills"\
                              " you. Better luck next time"+end)
                        input("Press enter to exit.")
                        sys.exit()
            elif("run" in choice.lower()):
                print("The dragon is to smart for you to escape from")
                monster(monsterInt,strength,enemKilled,invtor)
            else:
                print("False input")
                monster(monsterInt,strength,enemKilled,invtor)

        else:
            print(red +"A slime monster appears in front of you!" + end\
                  + " Use Attack or Run")
            choice = input("What will you do? ")
            if("attack" in choice.lower()):
                if("Axe" in invtor):
                    print("You use your axe to attack and kill the monster")
                    enemKilled += 1
                    monsterLive = False
                elif("Sword" in invtor):
                    print("You use your sword to attack and kill the monster")
                    enemKilled += 1
                    monsterLive = False
                else:
                    print("You begin to punch the slim killing it.")
                    enemKilled += 1
                    monsterLive = False
            elif("run" in choice.lower()):
                print("You escaped the monster")
                monsterLive = False
            else:
                print("False input")
                monster(monsterInt,strength,enemKilled,invtor)
        return strength, enemKilled
