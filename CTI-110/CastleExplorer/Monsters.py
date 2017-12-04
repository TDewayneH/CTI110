import colorama, random, sys
colorama.init()

def monster(monsterInt, strength, invtor=[]):
    red = "\033[1;31m"
    blue = "\033[1;34m"
    end = "\033[0;0m"
    monsterLive = True
    if(monsterInt==3):
        monsterInt = 2
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
                        monsterLive = False
                    elif("Magic Amulet"):
                        print("You use your sword to attack the zombie"\
                              " But he was able to bite you." + red +\
                              " Your strength goes down 3. The amulet seems to"\
                              " have no effect on the zombies." + end)
                        strength -= 3
                        monsterLive = False
                    else:
                        print("You use your sword to attack the zombie"\
                              " But he was able to bite you." + red +\
                              " your strength goes down 3" + end)
                        strength -= 3
                        monsterLive = False
                else:
                    if("Suit of Armor" in invtor):
                        print("You have no weapon so you start to punch the"\
                              " zombie but he gets a few bites in on you"\
                              " before you kill him. Your armor saves you from damage")
                        monsterLive = False
                    elif("Magic Amulet" in invtor):
                        print("You have no weapon so you start to punch the"\
                              " zombie but he gets a few bites in on you"\
                              " before you kill him." + red +\
                              " Your strength goes down 5. The amulet seems"\
                              " to have no effect on the zombie" + end)
                        strength -= 5
                        monsterLive = False
                    else:
                        print("You have no weapon so you start to punch the"\
                              " zombie but he gets a few bites in on you"\
                              " before you kill him." + red +\
                              " Your strength goes down 5" + end)
                        strength -= 5
                        monsterLive = False
            elif("run" in choice.lower()):
                if(random.randint(1,2) == 2):
                    print("You escaped the monster")
                    monsterLive = False
                else:
                    print(red+"You faild to escape"+end)
                    monster(monsterInt,strength,invtor)
            else:
                print("False input")
                monster(monsterInt,strength,invtor)
                    
        elif(monsterInt == 2):
            print(red + "A wolf appears in front of you!" + end +\
                  " Use Attack or run.")
            choice = input("What will you do? ")
            if("attack" in choice.lower()):
                if("Axe" in invtor):
                    print("You use your axe and cut the wolf down!")
                    monsterLive = False
                elif("Sword" in invtor):
                    if("Suit of Armor" in invtor):
                        print("You use your sword to attack the wolf"\
                              " But he tried to bite you but your armor"\
                              " saved you from it")
                        monsterLive = False
                    elif("Magic Amult" in invtor):
                        print("You have no weapon so you start to punch the"\
                              " zombie but he gets a few bites in on you"\
                              " before you kill him." + red +\
                              " Your strength goes down 3 The amult has"\
                              " no effect on the wolf" + end)
                        strength -= 3
                        monsterLive = False
                    else:
                        print("You use your sword to attack the wolf"\
                              " But he was able to bite you."\
                              " Your strength goes down 3."+end)
                        strength -= 3
                        monsterLive = False
                else:
                    if("Suit of Armor" in invtor):
                        print("You have no weapon so you start to punch the"\
                              " wolf but he gets a few bites in on you"\
                              " before you kill him. Your armor saves you from damage")
                        monsterLive = False
                    elif("Magic Amulet" in invtor):
                        print("You have no weapon so you start to punch the"\
                              " wolf but he gets a few bites in on you"\
                              " before you kill him." + red +\
                              " Your strength goes down 5"\
                              " The amult has no effect on the wolf" + red)
                        strength -= 5
                        monsterLive = False
                    else:
                        print("You have no weapon so you start to punch the"\
                              " wolf but he gets a few bites in on you"\
                              " before you kill him." + red +\
                              " Your strength goes down 5" + end)
                        strength -= 5
                        monsterLive = False
            elif("run" in choice.lower()):
                if(random.randint(1,2) == 2):
                    print("You escaped the monster")
                    monsterLive = False
                else:
                    print(red+"You faild to escape"+end)
                    monster(monsterInt,strength,invtor)
            else:
                print("False input")
                monster(monsterInt,strength,invtor)
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
                        monsterLive = False
                    else:
                        print("You use your axe to attack the dragon!"\
                              " He is very powerful." + red + " You lose"\
                              " 10 strength"+end)
                        strength -= 10
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
                        monsterLive = False
                    else:
                        print("You use your sword to attack the dragon!"\
                              " He is very powerful." + red +" You lose"\
                              " 15 strength")
                        strength -= 15
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
                        sys.exit()
            elif("run" in choice.lower()):
                print("The dragon is to smart for you to escape from")
                monster(monsterInt,strength,invtor)
            else:
                print("False input")
                monster(monsterInt,strength,invtor)
        else:
            print(red +"A slime monster appears in front of you!" + end\
                  + " Use Attack or Run")
            choice = input("What will you do? ")
            if("attack" in choice.lower()):
                if("Axe" in invtor):
                    print("You use your axe to attack and kill the monster")
                    monsterLive = False
                elif("Sword" in invtor):
                    print("You use your sword to attack and kill the monster")
                    monsterLive = False
                else:
                    print("You begin to punch the slim killing it.")
                    monsterLive = False
            elif("run" in choice.lower()):
                print("You escaped the monster")
                monsterLive = False
            else:
                print("False input")
                monster(monsterInt,strength,invtor)
        return strength
