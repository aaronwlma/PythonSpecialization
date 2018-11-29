# Assignment 02b - Chapter 2
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 1 - Programming for Everybody (Getting Started with Python)

# Problem: 2.3 Write a program to prompt the user for hours and rate per hour using
# input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test
# the program (the pay should be 96.25). You should use input to read a string
# and float() to convert the string to a number. Do not worry about error
# checking or bad user data.

# Prompt user to provide valid data input
hrs = input("Enter hours: ")
rate = input("Enter rate per hour: ")

# Calculate the gross pay based on the float values
pay = float(hrs) * float(rate)

# Print result and output
# print("Pay: " + str(pay))
print("Pay:", pay)
