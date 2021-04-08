#Author: Kunal Kale
#Date: 08/04/2021
#Description: A program with cubic running time. 
# Read in N integers and counts the   number of triples that sum to exactly 0

#Function to find triplets in the array
def find_triplets(arr,noOfValues):
    count = 0
    for i in range(0,noOfValues-2):
        for j in range(i+1,noOfValues-1):
            for k in range(j+2,noOfValues):
                sum = arr[i]+arr[j]+arr[k]
                if(sum == 0):
                    print(arr[i],arr[j],arr[k])
                    count += 1
    return count

#Function to count the triplets
def check_triplets(noOfTriplets):
    if(noOfTriplets == 0):
        print("No triplets found")
    else:
        print(noOfTriplets," triplets found")

#Function for User Input
def user_input():
    try:
        noOfValues = int(input("Enter size of array: "))
        arr = []
        for i in range(noOfValues):
            value = int(input(f"Enter value for arr[{i}]: "))
            arr.append(value)
        return arr, noOfValues
    except Exception:
        print("Invalid Input")

#Driver class
arr, noOfValues = user_input()
noOfTriplets = find_triplets(arr,noOfValues)
check_triplets(noOfTriplets)
