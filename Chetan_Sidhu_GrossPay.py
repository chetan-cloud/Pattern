#Assignment: Gross pay calculator
#Class: PROG 108
#Date: 1/9/22
#Author: Chetan Sidhu
#Description: Program to calculate the gross pay given hours and hourly rate

print("Welcome to Gross Pay Calculator")

print()

hours = int(input("Hours Worked: "))

pay = int(input("Hourly Pay Rate: "))

total = hours * pay

print()

print("Gross Pay: " + str(total))
