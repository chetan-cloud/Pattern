#Assignment: Coffee Shop Invoice
#Class: PROG 108
#Date: 1/19/22
#Author: Chetan Sidhu
#Description: Invoice for AM Coffee Shop

line1 = ("*" * 50)

print(line1)

print("Welcome to AM Coffee Shop")

print(line1)

print("     /\      |\    /|")
print("    /  \     | \  / |")
print("   /    \    |  \/  |")
print("  /------\   |      |")
print(" /        \  |      |")
print("/          \ |      |")
print(line1)

print()

date = int(input("Please enter date of the month (1-31): "))

coffee = int(input("Please enter the amount of coffee in pounds: "))

print()

print(line1)

line2 = ("-" * 50)

print(line2)

ship = coffee * .65 + 2.5

print("Shipping cost: " + str(ship))

print(line2)

print("Date" , " Cost", " Tax", " Total (Cost + Shipping + Tax)", sep="\t|")

print(line2)

cost = 9.50 * coffee

tax = 31 - date

tax /= 5

tax /= 100

tax *= cost

tax = round(tax, 2)

total= cost + tax + ship

print(date, cost,  tax, total , sep="\t| ")

print(line2)

date += 1

tax = 31 - date

tax /= 5

tax /= 100

tax *= cost

tax = round(tax, 2)

total= cost + tax + ship

print(date, cost,  tax, total , sep="\t| ")

print(line2)

date += 1

tax = 31 - date

tax /= 5

tax /= 100

tax *= cost

tax = round(tax, 2)

total= cost + tax + ship

print(date, cost,  tax, total , sep="\t| ")

print(line2)

print("Bye")
