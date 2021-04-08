#Author: Kunal Kale
#Date: 08/04/2021
#Description: A library for reading in 2D arrays of integers, doubles, or booleans 
# from standard input and printing them out to standard output.

#Function for Two Dimentional Array
def twoD_Array(m,n):
    rows, cols = (m, n)
    array = []
    for i in range(rows):
        column = []
        for j in range(cols):
            value = int(input(f"Enter the value [{i}][{j}]: "))
            column.append(value)
        array.append(column)
    return array

#Function for User Input
def user_input():
    try:
        m = int(input("Enter no of rows: "))
        n = int(input("Enter no of columns: "))
        return m, n
    except Exception:
        print("Invalid Input")

#Driver Class
m, n = user_input()
arr = twoD_Array(m,n)
print("2D Array")
print(arr)