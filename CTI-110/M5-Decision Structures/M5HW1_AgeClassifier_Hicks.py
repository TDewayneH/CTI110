#CTI-110
#M5HW1 - Age Classifier
#Dewayne Hicks
#8NOV17

def main():
    
    #Ask user their age
    age = int(input("What is your age padawan, if you are younger than 1 round"\
                    " up also how are you using a computer?!?: "))

    #If user is one or younger
    if(age<=1):                 
        print("You are an infant and the darkside shall consume you!")
        
    #If user is between 1 and 13
    elif(age<13):     
        print("You are a child and the darkside can still consume you!")
        
    #if user is between 13 and 20
    elif(age<20):   
        print("You are a teenager and might be able to fight the darkside for"\
              " a time!")
        
    #if user is 20 or over
    else:                       
        print("You are an adult and have a good chance to fight the darkside!")


main()

input("\n\nPress enter to exit")
