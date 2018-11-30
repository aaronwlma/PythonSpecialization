# Assignment 03a - Chapter 3
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 1 - Programming for Everybody (Getting Started with Python)

# Problem: 3.1 Write a program to prompt the user for hours and rate per hour
# using input to compute gross pay. Pay the hourly rate for the hours up to 40
# and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45
# hours and a rate of 10.50 per hour to test the program (the pay should be
# 498.75). You should use input to read a string and float() to convert the
# string to a number. Do not worry about error checking the user input - assume
# the user types numbers properly.

# Retrieve hours worked and rate
hours = input("Enter Hours: ")
h = float(hours)
rate = input("Enter Rate per Hour: ")
r = float(rate)

# If hours worked is less than 40, calculate normally
if h <= 40 :
    pay = r*h
    print(pay)
# If hours worked is more than 40, calculate with overtime rate
else :
    pay = r*40+1.5*r*(h-40)
    print(pay)
