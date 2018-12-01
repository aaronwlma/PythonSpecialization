# Assignment 05a - Chapter 5
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 1 - Programming for Everybody (Getting Started with Python)

# Problem: 5.2 Write a program that repeatedly prompts a user for integer
# numbers until the user enters 'done'. Once 'done' is entered, print out the
# largest and smallest of the numbers. If the user enters anything other than
# a valid number catch it with a try/except and put out an appropriate message
# and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

# Assignment 06 - Chapter 6
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 2 - Python Data Structures

# Problem: 6.5 Write code using find() and string slicing (see section 6.10) to
# extract the number at the end of the line below. Convert the extracted value
# to a floating point number and print it out.


text = "X-DSPAM-Confidence:    0.8475";
index = text.find('0.8475')
print(float(text[index:index + 6]))
