# -*- coding: utf-8 -*-
"""
Jay Yang
Lab 7
Created on Thu Sep 26 18:37:33 2019
"""

"""
INPUT: number of layers for the triangle
OUTPUT: block of string looking like an isoceles triangle
for example:
    =
   ===
  =====
 =======

ALGORITHM: 
    Start of while Loop:
       1. prompt user to choose the number of layers of the triangle
       2. concatenate '=' and ' ' to the current string to both left and right
       3. skips a line every iteration to go to the next layer of the triangle
       4. return the string
    End of loop:
"""
import sys
import os

# DEFINING FUNC
def building2DPyramid(symbol, layers):
    count = 0
    center = symbol
    space = " "*len(symbol)
    while layers > 0 and count < layers-1:
        if count == 0:
            print(space*(layers-count) + symbol + space*(layers-count))
        count += 1
        center = symbol + center + symbol
        wholeLayer = space*(layers-count) + center + space*(layers-count)
        print(wholeLayer)
    return ""

def game():
    symbol = input("Choose the look for the brick/the symbol(string of any length) of the 2D pyramid:\n")
    if len(symbol) == 0:
        print("Enter something.")
        counter = 0
        while len(symbol) == 0:
            symbol = input("Try again, with something longer than nothing:")
            counter += 1
            if counter > 3:
                break;
        if counter > 3 and len(symbol) == 0:
            print("""............................................________ 
    ....................................,.-'"...................``~., 
    .............................,.-"..................................."-., 
    .........................,/...............................................":, 
    .....................,?......................................................, 
    .................../...........................................................,} 
    ................./......................................................,:`^`..} 
    .............../...................................................,:"........./ 
    ..............?.....__.........................................:`.........../ 
    ............./__.(....."~-,_..............................,:`........../ 
    .........../(_...."~,_........"~,_....................,:`........_/ 
    ..........{.._$;_......"=,_......."-,_.......,.-~-,},.~";/....} 
    ...........((.....*~_......."=-._......";,,./`..../"............../ 
    ...,,,___.`~,......"~.,....................`.....}............../ 
    ............(....`=-,,.......`........................(......;_,,-" 
    ............/.`~,......`-...................................../ 
    .............`~.*-,.....................................|,./.....,__ 
    ,,_..........}.>-._...................................|..............`=~-, 
    .....`=~-,__......`,................................. 
    ...................`=~-,,.,............................... 
    ................................`:,,...........................`..............__ 
    .....................................`=-,...................,%`>--==`` 
    ........................................_..........._,-%.......` 
    ..................................., """)
            print("\n")
        
    while len(symbol) != 0: 
        try:
            layers = int(input("Enter a positive integer for the number of layers for the 2D pyramid:" ))
            if layers == 1:
                print("One layer pyramid? Let's not be boring. ")
                continue
            elif layers == 0:
                print("¯\_(ツ)_/¯")
                continue
            elif layers < 0:
                print("(╯°□°)╯︵ ┻━┻")
        except ValueError:
           print("That's not an integer!")
           continue
        else: break
    
    if len(symbol) > 0:
        print(building2DPyramid(symbol, layers))
    else: print("You make me sad!\n")

# MAIN
def main():
    # make below a method
    game()
    counter = 1
    while counter >= 1:
        rerun = input("Play again? Enter 'Y' or 'y' for Yes. Enter any other key to quit.")
        if rerun == "Y" or rerun == "y":
            game()
        else:
            print("Thanks for playing and Goodbye!")
            break


if __name__ == "__main__":
    main()
#    answer = raw_input("Do you want to restart this program ? ")
#    if answer.lower().strip() in "y yes".split():
