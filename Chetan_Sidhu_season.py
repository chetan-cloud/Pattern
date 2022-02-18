#Assignment: Seasons Detector
#Class: PROG 108
#Date: 1/26/22
#Author: Chetan Sidhu
#Description: Asks user for the month and day as integers and determines the season of this date

print("Welcome to the Seasons program")
month = int(input("Please enter the month (between 1 and 12) : "))
if month > 12 or month < 1:
    print("Invalid month entered." "\nExiting....")
else :
    day = int(input("Please enter the day (between 1 and 30) : "))
    if month == 1 and day > 31 or day < 1:
        print("Invalid day entered.", "\nExiting....")
    elif month == 3 and day > 31 or day < 1:
        print("Invalid day entered.", "\nExiting....")
    elif month == 5 and day> 31 or day < 1:
        print("Invalid day entered.", "\nExiting....")
    elif month == 8 and day> 31 or day < 1:
        print("Invalid day entered.", "\nExiting....")
    elif month == 7 and day > 31 or day < 1:
        print("Invalid day entered.", "\nExiting....")
    elif month == 10 and day>31 or day< 1:
        print("Invalid day entered.", "\nExiting....")
    elif month ==12 and day>31 or day < 1:
        print("Invalid day entered.", "\nExiting....")
    elif month == 2 and day > 28 or day < 1:
        print("Invalid day entered.", "\nExiting....")
    elif month == 4 and day > 30 or day < 1:
        print("Invalid day entered.", "\nExiting....")
    elif month == 6 and day>30 or day<1:
        print("Invalid day entered.", "\nExiting....")
    elif month ==9 and day> 30 or day <1:
        print("Invalid day entered.", "\nExiting....")
    elif month == 1 and day>30 or day < 1:
        print("Invalid day entered.", "\nExiting....")
    else :
        if month == 12 and day >= 16 or month == 1 or month == 2 or month == 3 and day <= 15:
            print("Season = Winter\nGood bye!")
        elif month == 3 and day >= 16 or month ==4 or month == 5 or month ==6 and day <= 15:
            print("Season = Spring\nGood bye!")
        elif month == 6 and day >= 16 or month == 7 or month ==8 or month == 9 and day <= 15:
            print("Season = Summer\nGood bye!")
        else:
            print("Season = Fall\nGood bye!")
        
     
    
