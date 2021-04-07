#Author: Kunal Kale
#Date: 07/04/2021
#Description: Program to Flip coin and print percentage of Heads and Tails

import re
import random
IS_HEAD, head, tail = 0, 0, 0
no_of_flips = int(input("Enter number of times to flip the coin: "))
posIntegerPatter = "^[1-9]\d*$"
result = re.match(posIntegerPatter,str(no_of_flips))
if(result):
    for i in range(no_of_flips):
        flip = random.randint(0,1)
        if(flip == IS_HEAD):
            head+=1
        else:
            tail+=1
    head_percent = head/no_of_flips*100
    tail_percent = 100-head_percent
    print("Heads percentage: ",head_percent)
    print("Tails percentage: ",tail_percent)
else:
    print("Invalid Input! Enter a valid Input")