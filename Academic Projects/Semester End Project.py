"""
CS22A Semester Project Fall 2019
Description: Term Project 
Input/Output: user's guess or response depending on the game mode selected
Collaborators: Saurob Kumar, Yvonna Leung, Jay Yang
"""

#Program welcomes the user by name, provide game description

userName = input("What is your name? ")

print("Dear", userName, """
      ########################################################################
      ###Welcome to the Number Guessing Game! Here's how it will work:     ###
      ###Your goal is to guess the correct number between 0 and 100 with   ###
      ###  the lowest number of attempts.                                  ###
      ###You will get the option of picking between 3 different levels:    ###
      ###  easy, difficult, or switch.                                     ###
      ###In easy mode, you'll have an unlimited number of tries.           ###
      ###In difficult mode, you'll have a limited number of 7 guesses.     ###
      ###In switch mode, you will switch places with the computer and have ###
      ###  the computer guess a number between 0-100.                      ###
      ###If you wish to terminate the game, press q/Q any time to quit.    ###
      ###                      Now let the fun begin!                      ###
      ########################################################################
      """)

import random

score = {'Rounds Played': 0, 'Wins': 0, 'Record': 0, 'Round Statistics': []  } 
top10 = open('top10.txt', 'a')

def easyMode():
    userGuessMode(True, 0)

def difficultMode():
    userGuessMode(False, 7) #number of tries as 7
    
def menu():    
    shouldRepeat = True
    while shouldRepeat: #set up a while loop to ask the user continuously for menu options
        print()
        print("1. Easy Mode 2. Difficult Mode 3. Switch Mode 4. View Scoreboard 5. Erase Scores")
        menu_choice = input("Choose a game mode (1-4) and 'q' to quit the program:")
        if menu_choice.upper() == 'Q':
            shouldRepeat = False
            print('Have a nice day!')
        elif menu_choice == '1':
            easyMode() #call the easy mode function
        elif menu_choice == '2': 
            difficultMode() #call difficult mode function
        elif menu_choice == '3':
            switchMode() #call switch mode function
        elif menu_choice == '4':
            scoreboard = open('scoreboard.txt', 'a')
            scoreboard.write('\nRounds Played: ' + str(score['Rounds Played']) + '\n')
            scoreboard.write('Wins: ' + str(score['Wins']) + '\n')
            scoreboard.write('Record: ' + str(score['Record']) + '\n')
            scoreboard.write('Game Statistcs: ' + str(score['Round Statistics']) + '\n')
            scoreboard.close()
            scoreboard = open('scoreboard.txt', 'r')
            scoreb = scoreboard.read()
            print('\n =========================== SCORE BOARD =========================== \n')
            print('\n', scoreb, '\n')
            topten = open('top10.txt', 'r')
            print("the top 10 least guesses are:", "\n", topten.read()) # make a neat table to display scoreboard
        elif menu_choice == '5':
            scoreboard = open('scoreboard.txt', 'w')
            scoreboard.close()
            top10 = open('top10.txt', 'w')
            top10.close()
            print('data erased')
        else:
            print('choose from 1 to 4 please:')
        # end of menu()
        
def modeRange():
            # Computer picks a random number that the user will try to guess
    ask = input("Enter 'd' for default range or 'c' for custom range or 'q' to go back to the menu. ")
    if ask.lower() == 'q':
        return
    elif ask == 'c':
        print('Custom Range: if lower range is bigger or equal to high range, then the two number will switch places.')
        flag = True
        while flag:
            low = input("Enter the lower end of your range or 'q' to go back to the menu. ")
            if low.upper() == 'Q':
                flag = False
                return
            else:
                try:
                    low = int(low)
                    #low = int(input("Enter the lower end of you range: "))
                    flag = False
                except ValueError:
                    print("Enter an integer please. ")

        # loop to capture high and handle exceptions
        flag = True
        while flag:
            high = input("Enter the higher end of you range or 'q' to go back to the menu. ")                
            if high.upper() == 'Q':
                flag = False
                return
            else:
                try:
                    high = int(high)
                    flag = False
                except ValueError:
                    print("Enter a number please. ")
        # if low >= high, low and high switch places
        if low > high:
            newLow = high
            newHigh = low
            high = newHigh
            low = newLow
        computerNumber = random.randint(low, high)
    elif ask == 'd':
        computerNumber = random.randint(0, 100)            
    else:
        print('Enter a valid option please.')
        return
    
    numTries = 0
    numbersGuessed = []
    guessedCorrectly = False
        
def userGuessMode(isEasyMode, guessLimit):
    playAgain = True
    status = ' '
    if isEasyMode == True:
        mode = 'easy'
    elif isEasyMode == False:
        mode = 'difficult'
    else:
        mode = 'switch'
    
    # Start of the core of the program.
    while playAgain:
        
        # Computer picks a random number that the user will try to guess
        ask = input("Enter 'd' for default range or 'c' for custom range or 'q' to go back to the menu. ")
        if ask.lower() == 'q':
            return
        elif ask == 'c':
            print('Custom Range: if lower range is bigger or equal to high range, then the two number will switch places.')
            flag = True
            while flag:
                low = input("Enter the lower end of your range or 'q' to go back to the menu. ")
                if low.upper() == 'Q':
                    flag = False
                    return
                else:
                    try:
                        low = int(low)
                        #low = int(input("Enter the lower end of you range: "))
                        flag = False
                    except ValueError:
                        print("Enter an integer please. ")

            # loop to capture high and handle exceptions
            flag = True
            while flag:
                high = input("Enter the higher end of you range or 'q' to go back to the menu. ")                
                if high.upper() == 'Q':
                    flag = False
                    return
                else:
                    try:
                        high = int(high)
                        flag = False
                    except ValueError:
                        print("Enter a number please. ")
            # if low >= high, low and high switch places
            if low > high:
                newLow = high
                newHigh = low
                high = newHigh
                low = newLow
            computerNumber = random.randint(low, high)
        elif ask == 'd':
            computerNumber = random.randint(0, 100)            
        else:
            print('Enter a valid option please.')
            return
        
        numTries = 0
        numbersGuessed = []
        guessedCorrectly = False

        # If it's easy mode, the number of guesses are unlimited (ignore the guessLimit); 
        #if you pass in fewer number of tries than 0, it's not valid, so it keeps repeating
        # If the number of tries is less than the guess limit (have not hit the guess limit)

        while not guessedCorrectly and (isEasyMode == True or numTries < guessLimit): 
            guessInput = input("Guess a number or enter 'q' to go back to the menu. ")
            if guessInput.lower() == 'q':
                return 
            else:
                userGuess = int(guessInput)
                         
            numTries += 1
            numbersGuessed.append(userGuess)
            if userGuess > computerNumber:
                print("Your number is higher than the correct value. Please try again.")
            elif userGuess == computerNumber: 
                guessedCorrectly = True
                print("Hooray! You guessed the correct number!")
                print("The number of tries to get the correct number is:", numTries)
                score['Wins'] += 1 #keep track of wins
                status = 'win'
                score['Rounds Played'] += 1 #keep track of the number of round
                
                if score['Record'] == 0:
                # This must be the first game, since it's impossible to get 0 tries
                    score['Record'] = numTries
                    top10.write(str(numTries) + '\n')

                elif numTries < score['Record']:
                # The score from this game is better than the record, so it is now the record.
                    score['Record'] = numTries #keep track of best record
                    top10.write(str(numTries) + '\n')

            else:
                print("Your number is lower than the correct value. Please try again.")

        if not guessedCorrectly:
            score['Rounds Played'] += 1 #keep track of the number of round
            print("You did not guess correctly! :( ")
            status = 'loss'
        
        score['Round Statistics'].append('round number: ' + str(score['Rounds Played']))
        score['Round Statistics'].append('game status: ' + status)
        score['Round Statistics'].append('the actual number: ' + str(computerNumber))
        score['Round Statistics'].append('numbers guessed: ' + str(numbersGuessed))
        score['Round Statistics'].append('game mode: ' + mode)
        score['Round Statistics'].append('number of tries: ' + str(numTries))
        
        playAgainInput = input("Would you like to play again in this Mode? Enter Y/N. ")
        if playAgainInput.lower() != "y":
            playAgain = False #will go back to main menu


###SWITCH MODE FUNCTION###

def switchMode():
    flag = True
    while flag:
        l = input("Enter the lower end of your range or 'q' to go back to the menu. ")
        if l.upper() == 'Q':
            flag = False
            return
        else:
            try:
                l = int(l)
                flag = False            
            except ValueError:
                print('Please enter a number.')

    flag = True
    while flag:
        u = input("Enter the upper end of your range or 'q' to go back to the menu. ")
        if u.upper() == 'Q':
            flag = False
            return
        else:
            try:
                u = int(u)
                flag = False            
            except ValueError:
                print('Please enter a number.')
                
    flag = True
    while flag:
        chance = input("Enter the number of chances I have or 'q' to go back to the menu. ")
        if chance.upper() == 'Q':
            flag = False
            return
        else:
            try:
                chance = int(chance)
                flag = False            
            except ValueError:
                print('Please enter a number.')
    num = random.randint(l, u)
    answer = ' '
# have to get rid of the number that appeared before.    
#answer = input("Is the number you picked " + str(num) + "? Enter 'y/Y' for Yes, else No: ")
#    while answer.upper() != 'Y':
    print("\nguessing started.\n")
    count = 0
    flag = True
    while count < chance and answer.upper() != 'Y' and flag == True:
        count += 1
        var = ''
        if count == 1:
            var = 'st'
        elif count == 2:
            var = 'nd'
        elif count == 3:
            var = 'rd'
        else:
            var = 'th'
        print("the " + str(count) + var + " guess.")
        answer = input("Is the number " + str(num) + " ? You can say y/Y(for yes), b/B(too big), s/S,(too small), q/Q(quit). ")
#        direct = input("Okay, is it too big or too small? Enter 'b/B' for too big, 's/S' for too small?")
        if answer.upper() == 'Q':
            print("Bye~")
            flag = False
        elif answer.upper() == 'B' and l != u:
            u = num - 1
            num = random.randint(l, u) 
            print('the new range is:', l, u)
        elif answer.upper() == 'S' and l != u:
            l = num + 1
            num = random.randint(l, u)
            print('the new range is:', l, u)
        elif l == u:
            print("There's only one number left. The answer is: " + str(l))
            answer = 'y'
        elif answer.upper() == 'Y':
            print("I got the nuuumberrrrr!")
        else:
            print("Please enter a valid option.")
            count -= 1

"""
MAIN()MAIN()MAIN()MAIN()MAIN()MAIN()MAIN()MAIN()MAIN()MAIN()MAIN()MAIN()
"""
#main
menu()
