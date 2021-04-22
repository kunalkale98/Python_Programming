'''
Author: Kunal Kale
Date: 13-04-2021
Description: JSON File Handling using Pyhton
'''

import json

#Function to read json file data
def readfile(file):
  with open(file,'r') as f:
    data = json.load(f)
    for emp in data['employee']:
      print(emp)

#Function to append to json file
def appendtofile(file):
  new_data = {"name": "Virat","email": "virat@gmail.com","city": "Delhi"}
  with open(file) as f:
    data = json.load(f)
    temp = data['employee']
    temp.append(new_data)
  with open(file,'w') as f:
    json.dump(data, f, indent=2)

#Driver Function
file = 'sample.json'
readfile(file)
appendtofile(file)
readfile(file)
