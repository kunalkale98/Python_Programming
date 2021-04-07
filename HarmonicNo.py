#Author: Kunal Kale
#Date: 07/04/2021
#Description: Program to prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N 

number = int(input("Enter a number to get it's Harmonic value: "))
harmonicNo = 0
for value in range(1,number+1):
    harmonicNo = harmonicNo + 1/value
print(harmonicNo)