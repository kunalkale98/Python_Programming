#Author: Kunal Kale
#Date: 07/04/2021
#Description: Program to take username as input from user and validate it 
#to print a Welcome message displaying the username

import re
userName = input ('Enter User Name:')
userName_Pattern = '^[A-Za-z]{3,}$'
result = re.match(userName_Pattern, userName)
if result:
    message = 'Hello ' + userName + ' , How are you?'
    print(message)
else:
    print('Invalid username')