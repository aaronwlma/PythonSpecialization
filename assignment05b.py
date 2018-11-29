# Assignment 05a - Chapter 5
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 1 - Programming for Everybody (Getting Started with Python)

# Problem: 5.2 Write a program that repeatedly prompts a user for integer
# numbers until the user enters 'done'. Once 'done' is entered, print out the
# largest and smallest of the numbers. If the user enters anything other than
# a valid number catch it with a try/except and put out an appropriate message
# and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# Initialize varibles
largest = None
smallest = None

# Statement to prompt input and evaluate
while True :
    # Prompt and check input
    num = input('Enter a number: ')
    if num == "done" :
        break
    try :
        numFloat = float(num)
    except :
        print('Invalid input')
        continue

    # Check initial value
    if largest == None or smallest == None :
        if largest == None :
            largest = numFloat
        else :
            smallest = numFloat
    # Evaluate value
    elif numFloat > largest :
        largest = numFloat
    elif numFloat < smallest :
        smallest = numFloat

# Print the desired output
print('Maximum is', int(largest))
print('Minimum is', int(smallest))
