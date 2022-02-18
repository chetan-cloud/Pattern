#Assignment: Tip Calculator
#Class: PROG 108
#Date: 2/11/22
#Author: Chetan Sidhu
#Description: calculates three options for an appropriate tip after a meal at a restaurant

print("Welcome to Tip Calculator")
print()

line = "-" *50
cost = float(input("Cost of meal: "))
while cost <= 0:
    print("Please enter a positive amount.")
    cost = float(input("Cost of meal: "))
print(line)
for i in range(15, 30, 5):
    print("Tip: " + str(i) +"%")
    i /= 100
    tip = cost * i
    total = cost + tip
    total = round(total, 2)
    print("Total amount including tip:$" + str(total)) 
    print(line)
print("Goodbye!")
                
