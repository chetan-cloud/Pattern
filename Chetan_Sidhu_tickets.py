#Assignment: Tickets
#Class: PROG 108
#Date: 2/11/22
#Author: Chetan Sidhu
#Description: calculates the total price of movie tickets purchased at a theater

print("Welcome to Funnyville Theater Ticket Counter.")

moreinput= "y"
total = 0

while moreinput.lower() == "y":
    print()
    type1 = input("Enter ticket type (A for advance/S for same day): ")
    age = int(input("Enter the age: "))
    print()
    if (type1.lower() == "a" or type1.lower() == "s") and age < 3:
        cost = 0
        
    elif type1.lower() == "a" and age >= 3 and age <=12:
        cost = 8
        
    elif type1.lower() == "a" and age >= 12:
        cost = 12
    elif type1.lower() == "s" and age >= 3 and age <=12:
        cost = 10
    elif type1.lower() == "s" and age >= 12:
        cost = 15
    
    print("Current ticket price: $" + str(cost))
    total +=cost
    print("Total so far: $" +str(total))
    print()
    moreinput = input("More tickets?(y/n)? ")
print()    
print("Final ticket pruice: $" +str(total))
print("Good bye!")
