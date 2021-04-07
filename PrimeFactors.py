#Author: Kunal Kale
#Date: 07/04/2021
#Description: Program to compute prime factorization of a Number entered by user

import math
number = int(input("Enter a no to find its Prime Factors: "))
while(number%2 == 0):
    print (2)
    number /= 2
i = 3
while(i <= int(math.sqrt(number))):
    while(number%i == 0):
        print (i)
        number /= i
    i += 2
if(number>2):
    print (int(number))


