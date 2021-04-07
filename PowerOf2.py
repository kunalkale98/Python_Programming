#Author: Kunal Kale
#Date: 07/04/2021
#Description: This program takes a command-line argument N 
#and prints a table of the powers of 2 that are less than or equal to 2^N.

number = int(input("Enter a number: "))
if(0<=number<31):
    for value in range(1,number+1):
        power = 2 ** value
        print("2^",value," = ",power)
else:
    print("Enter a number less than 31")