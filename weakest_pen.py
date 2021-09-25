#Need to import time module for managing dates
import time
from datetime import datetime

#birthday_book is a file containing birthdays stored as a dictionary for anyone you want a reminder for
from birthday_book import *

#Eventually need to revise to account for time zones
today = time.strftime('%d.%m')
year = time.strftime('%Y') 

#Empty list for storing today's birthdays
todays_birthdays = []

#For loop checkings birthdays against today's date and appending the [birthday, name] to todays_birthdays
for birthday, name in birthdays:
    if today in birthday:
        age = int(year) - int(birthday[-4:])
        todays_birthdays.append([age, name])

#This converts output from a nest list to a user-friendly view
def print_birthdays(list):
    print("---------------------")
    #Checks to make sure at least one person has a birthday today
    if todays_birthdays == []:
        print('No birthdays today.')
    #Formats list of birthdays
    else:
        print("Today's Birthdays:")
        print("")
        for birthday, name in list:
            print("{} turns {}".format(name, birthday))
    print("---------------------")

#Prints birthdays to the terminal
print_birthdays(todays_birthdays)