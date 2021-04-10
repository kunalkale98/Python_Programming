#Author: Kunal Kale
#Date: 09/04/2021
#Description: Program to generate N number of distinct coupon numbers, when N is taken as a user input 

import logs
import random

#Logger is defined to create error logs of the program
logger = logs.set_logger()

#Function to generate random number
def random_no():
    coupon = random.randrange(1,20)
    return coupon

#Function to get distinct coupon numbers
def distinct_coupon(noOfCoupons):
    arr = []
    flag = True
    randomNumbers = 0
    length = len(arr) 
    while(length < noOfCoupons):
        coupon = random_no()
        randomNumbers+=1
        if(length == 0):
            arr.append(coupon)
        else:
            for i in arr:
                if(coupon == i):
                    flag = False
                    break
                else:
                    flag = True
            if(flag == True):
                arr.append(coupon)
        length = len(arr)
    logger.info(arr)
    logger.info(f"Total {randomNumbers} random numbers needed")

#Driver Class
try:
    noOfCoupons = int(input("Enter number of coupons: "))
except Exception:
    logger.error("Invalid Input")
else:
    distinct_coupon(noOfCoupons)
