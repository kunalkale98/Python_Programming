'''
Author: Kunal Kale
Date: 13-04-2021
Description: CSV File Handling using Pyhton
'''

import csv
import logs
from csv import writer

#Function to read CSV file
def readfile(file):
    try:
        with open(file,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except Exception:
        logger.error("Can't read data")

#Function to write to the CSV file
def writetofile(file):
    try:
        with open(file,'a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([4,'Rahul','Punjab'])
            writer.writerow([5,'Hardik','Mumbai'])
    except Exception:
        logger.error("Error! Can't Update")

#Function to search data from CSV file
def searchdata(file):
    try:
        value = str(input("Enter name you want to search: "))
    except Exception:
        print("Invalid Input")
    try:
        with open(file,'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if(row[1] == value):
                    print(row)
    except Exception:
        logger.error("Error! Can't search data")

#Driver Function
if __name__=="__main__":
    logger = logs.set_logger()
    file  = 'sample.csv'
    readfile(file)
    searchdata(file)
    writetofile(file)
    readfile(file)