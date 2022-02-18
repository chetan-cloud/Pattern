#Assignment: Travel Time Calculator
#Class: PROG 108
#Date: 1/13/22
#Author: Chetan Sidhu
#Description: Calculates hours and minutes based of number of miles and mph

print("Welcome to the Trip Time Calculator")

traveled = float(input("Enter the miles traveled: "))

hour = float(input("Enter the miles per hour: "))

print("Estimated travel time")

hours = traveled // hour

minutes = traveled % hour

minutes = minutes / hour

minutes *= 60

hours = round(hours)

minutes = round(minutes)

print("Hours: " + str(hours))

print("Minutes: " + str(minutes))


                

