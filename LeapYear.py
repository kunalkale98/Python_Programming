#Author: Kunal Kale
#Date: 07/04/2021
#Description: Program to Find a year entered by user is a Leap year or Not

import re
year = int(input("Enter a Year: "))
yearPatter = "^\d{4}$"
result = re.match(yearPatter,str(year))
if(result):
    leapYear = year%4
    if(leapYear == 0):
        print(year," is a leap year")
    else:
        print(year," is not a leap year")
else:
    print("Invalid Year")