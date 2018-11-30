# Assignment 03b - Chapter 3
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 1 - Programming for Everybody (Getting Started with Python)

# Problem: 3.2 Take 3.1 and check against invalid inputs.

# Retrieve hours worked and rate
hours = input("Enter Hours: ")
rate = input("Enter Rate per Hour: ")

# Verify valid inputs
try :
    h = float(hours)
    r = float(rate)
except :
    print("Error, please enter numeric input")
    quit()

# If hours worked is less than 40, calculate normally
if h <= 40 :
    pay = r*h
    print(pay)
# If hours worked is more than 40, calculate with overtime rate
else :
    pay = r*40+1.5*r*(h-40)
    print(pay)
