#Assignment: Average MPG
#Class: PROG 108
#Date: 2/6/22
#Author: Chetan Sidhu
#Description: Computes Fuel Efficiency 

print("Welcome to the Average MPG Calculator")

line= "-" * 50
lasto = 0
print()
start = 0
start = int(input("Please enter the starting odemeter reading in miles: "))
lasto = start
moreinput= "y"
leg = 1
totalfuel = 0
totalmile = 0

while start <= 0:
    print()
    start = int(input("Invalid odemeter, please enter a positive number. "))

print()
while moreinput.lower() == "y":
    print(line)
    newo = int(input("Please enter the new odemeter reading in miles for leg #" + str(leg) + ": "))
    fuelnew = float(input("Please enter fuel consumed in gallons for leg #" + str(leg) + ": "))
    if lasto >= newo or fuelnew <= 0:
        print("Fuel consumed needs to be positive and new odometer reading needs to be higher than " + str(lasto))
    else:
        mpg = newo- lasto
        mpg /= fuelnew
        totalfuel += fuelnew
        totalmile += (newo - lasto)
        print("MPG for leg #" + str(leg) + " = " + str(mpg))
        moreinput = input("Continue (y/n)? ")            
        lasto = newo
        leg += 1
leg -= 1
print()
mpgtotal = totalmile / totalfuel 
print("Total number of legs in the journey: " + str(leg))
print("Final average MPG for the entire journey: "+ str(mpgtotal))
print("Bye!")

    

