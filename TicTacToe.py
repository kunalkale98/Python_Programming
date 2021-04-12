#Author: Kunal Kale
#Date: 10/04/2021
#Description: Program to play a Cross Game or Tic-Tac-Toe Game. 
# Player 1 is the User and the Player 2 is the Computer. 
# Computer take Random Cell on its turn and User will enter the position on its turn.

import random
import re
import logs

#Logger is defined to create error logs of the program
logger = logs.set_logger()

#Function to print the Board
def printBoard(board):
    print(" "+board['1']+" | "+board['2']+" | "+board['3']+" ")
    print('---+---+---')
    print(" "+board['4']+" | "+board['5']+" | "+board['6']+" ")
    print('---+---+---')
    print(" "+board['7']+" | "+board['8']+" | "+board['9']+" ")

#Function for User's Turn 
def userTurn(user,board):
    try:
        pos_pattern = '^\d{1}$' 
        position = str(int(input("Enter the position to make the move: ")))
        posResult = re.match(pos_pattern,position)
        if(posResult):
            if(board[position] == ' '):
                board[position] = user
            else:
                logger.info("Position not empty")
                userTurn(user,board)
        else:
            logger.error("Invalid Position Input")
            quit()
    except Exception:
        logger.error("Error! Enter a single digit number")
        quit()

#Function for Computer's Turn
def compTurn(comp,board):
    position = str(random.randint(1,9))
    if(board[position] == ' '):
        board[position] = comp
        printBoard(board)
    else:
        compTurn(comp,board)

#Function to check who Won:
def check_win(user,comp,board,winCombos):
    for combo in winCombos:
        userWin = 0
        compWin = 0
        for pos in combo:
            if(board[str(pos)] == user):
                userWin += 1
            if(userWin == 3):
                result = 'userWon'
                return result
        for pos in combo:
            if(board[str(pos)] == comp):
                compWin += 1
            if(compWin == 3):
                result = 'compWon'
                return result        
    if(count == 9):
        result = 'tie'
        return result
    return '0'

#Function to simulate the game
def game():
    board = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
    winCombos = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    printBoard(board)
    char = input("Enter Your Letter X or O:" )
    user = char.upper()
    count = 0
    print('You selected '+user)
    if(user != 'X' and user != 'O'):
        logger.error("Invalid Input for X or O")
        quit()
    else:
        if(user == 'X'):
            comp = 'O'
        else:
            comp = 'X'
    while(True):
        userTurn(user,board)
        count+=1
        compTurn(comp,board)
        count+=1
        if(count >= 5):
            result = check_win(user,comp,board,winCombos)
            if(result == 'userWon'):
                logger.info("You Won")
                break
            elif(result == 'compWon'):
                logger.info("Computer Won")
                break
            elif(result == 'tie'):
                logger.info("Its a Tie")
                break

    playAgain = input("Do you want to play again Y/N? ")
    restartPattern = '^[Y,N]{1}$'
    restartResult = re.match(restartPattern,playAgain.upper())
    if(restartResult):
        if(playAgain.upper() == 'Y'):
            game()
        elif(playAgain.upper == 'N'):
            logger.info("Thanks for playing.")
    else:
        logger.error("Invaild Input for Restart")
        quit()

#Driver Function
game()



