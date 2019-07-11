#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import random

from IPython.display import clear_output

def PlayerMarker(): #this function lets the player choose their letter
    
    
    letter = ''

    while not (letter == 'X' or letter == 'O'): #this while not loop is used for the players to pick ONLY X or O 
        #if the player chooses something other than X or O, the while not loop will continue to ask

        letter = input('Player 1 choose your marker! X or O?: ').upper() #Asks for user input
        print('\n')
        time.sleep(1)


# the first element in the list is the player 1 letter, the second is the player 2 letter.
    if letter == 'X':
        time.sleep(1)
        print('Player 1 is X and Player 2 is O')
        
        return ['X', 'O'] #Notice this, if player 1 chooses X, then X must be first in this list **REFER TO LINE 155**
        
    else:
        print('Player 1 is O and Player 2 is X')
        
        return ['O', 'X'] #Same here, if player 1 is O then 'O' must be first in the list. **REFER TO LINE 155**
        
def WhoGoesFirst(): #This function will automatically choose who goes first. 
    
    if random.randint(0,1) == 0: #a random integer is picked between only 0 and 1. So there is a 50/50 chance
        
        return 'Player 1' #Hence, if the rand int happens to be 0, player 1 would go first
        
    else: #otherwise, if the number is NOT 0 then player 2 goes first
        
        return 'Player 2'   
def PlayAgain(): #Basically a play again function after the game is a tie or a player wins
    
    play_again = input('Play again? (Y or N): ').lower()
    
    if play_again ==  'y':
        
        return 'y'
    else:
        return False
    
def isWinner(board, letter):

# Given a board and a player’s letter, this function returns True if that player has won.

    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # across the bottom
            (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
            (board[1] == letter and board[2] == letter and board[3] == letter) or # across the top
            (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
            (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
            (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
            (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
            (board[9] == letter and board[5] == letter and board[1] == letter)) # diagonal   

def MarkerSpot(board,letter,move): #assigns players letter to their choice of marker spot
    
    board[move] = letter #For example, a player chooses 8 for their 'move', the box where 8 is located is now their letter
    
def freeSpace(board,move): #this function checks to see if there is free space
    
    return board[move] == ' ' #Here, for whatever number box the player chooses, if it == to an empty string, then 
                              #there is indeed free space

def getPlayersMove(board): #This function is used for players to pick their marker spot by choosing a num from 1-9
    
    move = ' ' #this variable has an empty string, once players choose a number, that number goes into this var.
    
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpace(board,int(move)): 
        #This while loop is used so that players only choose numbers 1-9
        #If they dont choose a num 1-9, the while loop will continue to ask the player to choose a num 1-9
        #Notice there is an 'OR', this is because it will also check if there is free space for the spot that the 
        #player wants to choose. If there isn't free space, the loop will continue until the player picks a spot
        #where there is free space.
        
        move = input('Choose your spot! (1-9): ') #This is where the 'move' variable gets new input
        
    return int(move) #since input from users are returned in string format, it has to be converted into int format

def boardFull(board): #check if board is full
    for i in range(1,10): 
        if freeSpace(board,i): #this if statement will check every single box to see if it is empty
            return False #if it finds that there is at least one space open, it will return false and continue
    return True #if it doesn't find an empty box, the function will return True, and it will result in Tie Game
        

def display_board(board):
    # This is the official board to play the game.
    # Players will choose a number, and their marker will be placed in the box for which that number resides in
    
    
    print('   |   |')

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

    print('   |   |')
    
def boardFormat(): #this function is used to show the players what numbers to use so they can place their marker
    
    print('   |   |')

    print(' ' '1' ' | ' '2' ' | ' '3' )

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' '4' ' | ' '5' ' | ' '6' )

    print('   |   |')

    print('-----------')

    print('   |   |')

    print(' ' '7' ' | ' '8' ' | ' '9' )

    print('   |   |')

print("Welcome to Eric's Tic Tac Toe game!")

print('\n'*2)

time.sleep(1.0)

print('This is how the board layout looks like so you know where to place your marker!')

time.sleep(.5)

show_board = boardFormat()

print('\n'*2)

time.sleep(1.0)


while True:
    board = [' '] * 10 #this clears all spots on the board
    P1Letter, P2Letter = PlayerMarker() 
          #Notice 'P1Letter, P2Letter'. this had to be done this way so the
          #program could assign their correct letter to the correct player#
          #REFER TO LINE 22 or 27. if player one chose x then the list would be ['X','O']#
          #That is why P1Letter goes first in 'P1Letter, P2Letter' 
          #because the program will know that player 1 is X#
    print('\n'*2)
    time.sleep(1)
    turn = WhoGoesFirst() #executes function that choose random player to go first and assigns to variable 'turn'
    time.sleep(1)
    print(f'{turn} will go first!')
    time.sleep(1)
    gameIsPlaying = True
    
    
    while gameIsPlaying:
        if turn == 'Player 1':
            time.sleep(.5)
            display_board(board) #displays the board
            time.sleep(.5)
            print('***Player 1 GO***')
            boxnum = getPlayersMove(board) #Player picks move and their move is stored into a variable 'boxnum'
            print('\n'*2)
            time.sleep(.5)
            MarkerSpot(board,P1Letter,boxnum)
              #-here the function takes the players move which is now stored in 'boxnum' and assigns their 
              #letter into the box from where their number of choice was assigned to
          
            if isWinner(board,P1Letter): #Checks to see if player won after every turn.
                print('\n'*2)
                display_board(board)
                print('---Player 1 WON---')
                gameIsPlaying = False # makes the While loop False and triggers the PlayAgain function
            else:
                if boardFull(board): 
                      #if player hasn't won it will check to see if the board is full
                      #and if it isn't then it will continue to player 2
                      #however, if it is then it will result in Tie Game and trigger PlayAgain function
                    print('\n'*2)
                    display_board(board)
                    print('---TIE GAME!---')
                    gameIsPlaying = False
                else:
                    turn = 'Player 2'
                    
        else:
            display_board(board)
            print('***Player 2 GO***')
            boxnum = getPlayersMove(board)
            print('\n'*2)
            time.sleep(.5)
            MarkerSpot(board,P2Letter,boxnum)
            time.sleep(.5)
            if isWinner(board,P2Letter):
                print ('\n'*2)
                display_board(board)
                print('---PLAYER 2 WON---')
                gameIsPlaying = False
            else:
                if boardFull(board):
                    print('\n'*2)
                    display_board(board)
                    print('---TIE GAME!---')
                    break
                else:
                    turn = 'Player 1'
    if not PlayAgain():
        
        break
        
                         

None
# In[ ]:





# In[ ]:




