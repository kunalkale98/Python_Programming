#Author: Kunal Kale
#Date: 08/04/2021
#Description: A Program to simulates a gambler who start with stake and place fair $1 bets 
# until he/she goes broke or reach goal

import logging
import random

#To Create logs of the program when run, in a particular format
logging.basicConfig(filename='test.log',level=logging.DEBUG,
                    format='%(asctime)s:%(filename)s:%(levelname)s:%(message)s')

#Function for gambling with stake and goal as two parameters
def gambling(stake,goal):
    bets,win,broke = 0,0,0
    while(stake > broke and stake < goal):
        bets+=1
        outcome = random.randint(0,1)
        if(outcome == 1):
            win+=1
            stake+=1
        else:
            stake-=1
    if(stake == goal):
        logging.info("Gambler Won")
    else:
        logging.info("Gambler Lost")
    
    lost = bets - win
    logging.info(f"The gambler won {win} bets")
    logging.info(f"The gambler lost {lost} bets")
    winPercent = win/bets*100
    lostPercent = 100 - winPercent
    logging.info(f"Win Precentage:{winPercent}")
    logging.info(f"Lost Percentage:{lostPercent}")

#Function for User Input
def user_input():
    try:
        stake = int(input("Enter Gambler's Stake: "))
        goal = int(input("Enter Goal to achieve: "))
        return stake,goal
    except Exception:
        logging.error("Invalid Input")

#Driver Class
stake,goal = user_input()
gambling(stake,goal)