#!/usr/bin/env python3

#Greeting and current date and time
import datetime, RestAPI
now = datetime.datetime.now()
print("Well Hello There!")
print("The current time is " + str(now.strftime("%m/%d/%Y %I:%M:%S %p")))

#Type your username and press enter, this creates a new variable for username
UserName = input("Enter your name:\n")

#Print the value of the variable (UserName), which will display the input value
print("Username is: " + str(UserName))

#Type your age and press enter, this creates a new variable for the user's age
UserAge = int(input("Enter your age:\n"))
print("Your age is: " + str(UserAge))

#Ask user if they would like to call ipwhois API for IP data
IPQuery = input('Would you like to see additional information about your external IP Address?\n')
if IPQuery == 'y' or 'Y' or 'yes' or 'Yes' or 'YES' or '1':
    RestAPI.ipdata()
    print('\nGoodbye!')
else:
    print('Goodbye!')
