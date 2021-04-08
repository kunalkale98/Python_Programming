#Author: Kunal Kale
#Date: 08/04/2021
#Description: Program that takes two integer command-line arguments x and y and prints 
# the Euclidean distance from the point (x, y) to the origin (0, 0)


import math
#Function to find Euclidean Distance
def euclidean_distance(x,y):
    distance = math.sqrt(pow(x,2)+pow(y,2))
    return distance

#Function for User Input
def user_input():
    try:
        x = float(input("Enter X co-ordinate: "))
        y = float(input("Enter Y co-ordinate: "))
        return x,y
    except Exception:
        print("Invalid Input")

#Driver Class
x,y = user_input()        
distance = euclidean_distance(x,y)
print("Euclidean Distance: ",distance)