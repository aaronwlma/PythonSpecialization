# Assignment 03c - Chapter 3
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 1 - Programming for Everybody (Getting Started with Python)

# Problem: 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the
# score is out of range, print an error. If the score is between 0.0 and 1.0,
# print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and
# exit. For the test, enter a score of 0.85.

# Retrieve score received
score = input("Enter Score: ")

# Check to see if input can be casted to a float
try :
    scoreFloat = float(score)
except :
    print("Error, input cannot be casted to a float")
    quit()

# Check to see if input is a valid score
if scoreFloat > 1.0 or scoreFloat < 0.0 :
    print("Error, input is not a valid score")
# Evaluate score for proper grade output
elif scoreFloat <= 1.0 and scoreFloat >= 0.9 :
    print("A")
elif scoreFloat < 0.9 and scoreFloat >= 0.8 :
    print("B")
elif scoreFloat < 0.8 and scoreFloat >= 0.7 :
    print("C")
elif scoreFloat < 0.7 and scoreFloat >= 0.6 :
    print("D")
else :
    print("F")
