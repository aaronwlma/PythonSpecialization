# Assignment 04 - Chapter 4
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 1 - Programming for Everybody (Getting Started with Python)

# Problem: 4.6 Write a program to prompt the user for hours and rate per hour
# using input to compute gross pay. Pay should be the normal rate for hours up
# to 40 and time-and-a-half for the hourly rate for all hours worked above 40
# hours. Put the logic to do the computation of time-and-a-half in a function
# called computepay() and use the function to do the computation. The function
# should return a value. Use 45 hours and a rate of 10.50 per hour to test the
# program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a
# number. Do not worry about error checking the user input unless you want to -
# you can assume the user types numbers properly. Do not name your variable sum
# or use the sum() function.

# Function for computing pay based on hours worked and pay rate
def computepay(h,r) :
    if h <= 40 :
        pay = h * r
    else :
        pay = 40*r + 1.5*r*(h-40)
    return pay

# Retrieve inputs and cast to proper type
hours = input("Enter hours: ")
rate = input("Enter rate per hour: ")
try :
    hoursFloat = float(hours)
    rateFloat = float(rate)
except :
    print("Error, input values cannot be casted to floats")
    quit()

# Run defined function and print output
p = computepay(hoursFloat,rateFloat)
print(p)
