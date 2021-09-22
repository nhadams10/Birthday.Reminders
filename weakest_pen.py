#Need to import time module for managing dates
import time
from datetime import datetime

#Birthday_Book is a file containing birthdays for anyone you want a reminder for, written in the format: Day.Month.Year  First_Name Last_Name
#Might want to update the format of this at a later time
#Setting variable equal to file path
Birthday_Book = '/workspace/Birthday.Reminders/Birthday_Book.txt'

#Eventually need to revise to account for time zones
today = time.strftime('%d.%m.%Y')
print(today)

#A date for testing purposes
test_date = '22.08.2021'
print(test_date)

#Empty string for storing today's birthdays
todays_birthdays = ''

def birthday_checker():
    birthdays = open(Birthday_Book, 'r')
    for line in birthdays:
        if today in line:
            name = line.split('  ')[1]
            todays_birthdays += name
    #if todays_birthdays == "":
        #todays_birthdays = "No Birthdays Today"
    print(todays_birthdays)


