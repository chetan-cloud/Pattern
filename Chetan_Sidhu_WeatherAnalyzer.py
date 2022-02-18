#Assignment: Weather Analyzer
#Class: PROG 108
#Date: 1/23/22
#Author: Chetan Sidhu
#Description: Asks the user for current outside temp, and prints report.

print("Welcome to the Weather Analyzer")

print()

print()

unit = input("Please enter the units (Enter F for Fahrenheit/ C for Celsius) :")

if (unit != 'F' and unit != 'f' and unit != 'C' and unit != 'c'):
    print("Invalid units entered. Exiting")
else :
    temp = int(input("Please enter the outside temperature: "))
    if unit == 'c' or unit == 'C':
        temp = temp*9/5 +32
        print()
        print("It is " + str(temp) + " degrees outside.")
        if temp > 80 :
            print("It is too hot outside.")
        elif temp < 60:
            print("It is chilly outside.")
        else:
            print("It is very pleasant outside.")
    else:
        print()
        print("It is " + str(temp) + " degrees outside.")
        if temp > 80 :
            print("It is too hot outside.")
        elif temp < 60:
            print("It is chilly outside.")
        else:
            print("It is very pleasant outside.")
        
    
    
    

