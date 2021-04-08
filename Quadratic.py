#Author: Kunal Kale
#Date: 08/04/2021
#Description: Program to find the roots of the equation a*x*x + b*x + c

import cmath
#Function to get roots of the equation
def get_roots(a,b,c,delta):
    print(f"The equation is {a}X^2+{b}X+{c}")
    root1 = (-b + cmath.sqrt(delta))/(2*a)
    root2 = (-b - cmath.sqrt(delta))/(2*a)
    print(f"Root1:{root1} , Root2:{root2}")

#Function to get delta
def get_delta(a,b,c):
    delta = b*b - 4*a*c
    return delta

#Function for User Input
def user_input():
    try:
        a = float(input("Enter the value for a: "))
        b = float(input("Enter the value for b: "))
        c = float(input("Enter the value for c: "))
        return a,b,c
    except Exception:
        print("Invalid Input")

#Driver Class
a,b,c = user_input()
delta = get_delta(a,b,c)
get_roots(a,b,c,delta)