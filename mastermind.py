import random


def run_game():
    """
TODO: implement Mastermind code here
"""
    #################################################################################################
    '''
    generates 4 digit code and adds it a to empty list
    '''
    Chances_left =12

    digit_list = [0,0,0,0]
    for i in range(4):
        combo = random.randint(1,8)
        while str(combo) in digit_list:
            combo = random.randint(1,8)
        digit_list[i] =  str(combo)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    #print(digit_list)
    ################################################################################################# 
    '''
    takes user input,checks if its an integer
    makes sure its 4 numbers and that its more at 9 or less than 0
    '''
    while Chances_left >= 0 :
    #################################################################################################
        while True:
            Guess = input("Input 4 digit code: ")
            if len(Guess) == 4 :
                try:
                    len(Guess) < 4 or len(Guess) > 0
                    Guess=int(Guess)
                except : 
                    continue
                break       
            else:
                print("Please enter exactly 4 digits.")            
    #################################################################################################
        '''
        turns user input a str 
        then takes tht var and turns it into  a list so it can compare each number
        '''
        GuessSTR= str(Guess)
        guessList = list(GuessSTR)      #list of user input
        #digit_list = list(digit_list)   #list of rando numbers  
        Right_Guesses = 0
        Tries = 0 
    #################################################################################################
        '''
        takes the user input and loops through the number and 
        if it meets the following conditions then the following happens
        '''
        for i in range(4) :
            if guessList[i] == digit_list[i] :
                Right_Guesses += 1
            elif guessList[i] in digit_list : 
                Tries += 1
        right = str(Right_Guesses)
        
    #################################################################################################
        '''
        if the all the numbers are correct then do the following
        '''
        if right == "4":
            print("Number of correct digits in correct place:     "+str(Right_Guesses))    
            print("Number of correct digits not in correct place: "+str(Tries))
            print("Congratulations! You are a codebreaker!")  
            print("The code was: "+ GuessSTR)
            break        
        
        #if the user guesses wrong then the amount of chances decrements until its  0  
        
        elif Guess != digit_list :
            Chances_left -=1
            print("Number of correct digits in correct place:     "+str(Right_Guesses))
            print("Number of correct digits not in correct place: "+str(Tries))
            print("Turns left: "+str(Chances_left))
               
        #continue 
        if Chances_left == 0 :
            break
        
    #################################################################################################
if __name__ == "__main__":
    run_game()
