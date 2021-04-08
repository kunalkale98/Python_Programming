#Author: Kunal Kale
#Date: 08/04/2021
#Description: Program that takes two arguments from user temperature and wind velocity 
# and prints the wind chill

#Function to Calculate Wind Chill
def cal_windchill(temp,vel):
    windChill =  35.74 + 0.6215*temp + (0.4275*temp - 35.75)*pow(vel,0.16)
    print(f"WindChill is {windChill}")

#Function for User Input
def user_input():
    try:
        temperature = float(input("Enter Temperature in Fahrenheit: "))
        velocity = float(input("Enter Wind Speed in miles per hr: "))
        return temperature,velocity
    except Exception:
        print("Invalid Input")

#Driver Class
temp,vel = user_input()
if(vel > 120 or vel < 3 or temp > 50 ):
    print("Can't get WindChill at this Parameters")
else:
    cal_windchill(temp,vel)
