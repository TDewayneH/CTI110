#A guessing number game
#15NOV17
#CTI-110 M7HW2 - Guessing Game
#Dewayne Hicks

import random

numberToGuess = 0;
Guessing = True;
guess = "";
guessesLeft = 5;
picked = False;
hellMode=False;


print('Welcome to the guessing number game!');
print('Can you figure out what the number is??');
print ('Select your difficulty level!')
print ('1 = Easy, 2 = Normal, 3 = Hard, 4 = Mythic')
while picked == False:
    difficultyPick = int(input())
    if difficultyPick == 1:
        numberToGuess = random.randint (1, 10)
        guessesLeft = 5
        print('Pick from 1 - 10. With 5 guesses.')
        print('Are you sure you want this level? Yes or No.')
        answer = input()
        if(answer.lower().startswith("y")): 
            picked = True
        elif(answer.lower().startswith("n")):
            print('Ok please seletect a level')
        else:
            print('Please only put Yes or No, re-select your level.')

    elif difficultyPick == 2:
        numberToGuess = random. randint (1, 25)
        guessesLeft = 7
        print('Pick from 1 - 25. With 7 guesses.')
        print('Are you sure you want this level? Yes or No.')
        answer = input()
        if(answer.lower().startswith("y")): 
            picked = True
        elif(answer.lower().startswith("n")):
            print('Ok please seletect a level')
        else:
            print('Please only put Yes or No, re-select your level.')

    elif difficultyPick == 3:
        numberToGuess = random. randint (1, 50)
        guessesLeft = 10
        print('Pick from 1 - 50. With 10 guesses.')
        print('Are you sure you want this level? Yes or No.')
        answer = input()
        if(answer.lower().startswith("y")): 
            picked = True
        elif(answer.lower().startswith("n")):
            print('Ok please seletect a level')
        else:
            print('Please only put Yes or No, re-select your level.')

    elif difficultyPick == 4:
        numberToGuess = random. randint (1, 100)
        guessesLeft = 15
        print('Pick from 1 - 100. With 15 guesses.')
        print('Are you sure you want this level? Yes or No')
        answer = input()
        if(answer.lower().startswith("y")): 
            picked = True
        elif(answer.lower().startswith("n")):
            print('Ok please seletect a level')
        else:
            print('Please only put Yes or No, re-select your level.')
                   
    else:
        print('Invalid selection please pick a from 1-4!')

while guessesLeft > 0:
    if(hellMode==False):
        print('You have ' + str(guessesLeft) + ' guesses left!');
    print('What do you think the number is?');
    guess = int(input());
    if(guess != numberToGuess):
        if(guess > numberToGuess):
            print('Sorry that was not right, it was to high.');
            guessesLeft-=1;
        else:
            print('Sorry that was not right, it was to low.');
            guessesLeft-=1;
    else:
        if(hellMode==False):
            evolve = random.randint(1,4)    #This will pick if you trigger event
            if(evolve == 1):                #This will end the game
                print('Congulations you won!');
                break;
            else:
                if(difficultyPick!=4):      #This will only advance the level if it's not on 4
                    difficultyPick+=1
                    print('You infuriated the game causing it to evolve!\n The difficulty of the game has incrased to ' + str(difficultyPick) + '!')
                    if(difficultyPick==2):
                        numberToGuess = random. randint (1, 25)
                        guessesLeft = 7
                        print('Pick from 1 - 25. With 7 guesses.')
                    elif(difficultyPick==3):
                        numberToGuess = random. randint (1, 50)
                        guessesLeft = 10
                        print('Pick from 1 - 50. With 10 guesses.')
                    elif(difficultyPick==4):
                        numberToGuess = random. randint (1, 100)
                        guessesLeft = 15
                        print('Pick from 1 - 100. With 15 guesses.')
                    else:
                        print('This is an error!')
                else:
                    print('You beat the hardest difficulty so now you will have hell mode!')    #This activates hell mode
                    hellMode=True
                    numberToGuess = random. randint (1, 150)
                    guessesLeft = 13
                    print('You don\'t know the range or how many guesses you have! Good luck to you, you will need it!')
        else:
            print('I can\'t believe you beat the hardest level! Wow we are not worthy of your awesomeness!!')
                    
    
    
input("\n\nPress enter to exit.")
