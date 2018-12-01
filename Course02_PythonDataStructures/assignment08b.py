# Assignment 08b - Chapter 8
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 1 - Programming for Everybody (Getting Started with Python)

# Problem: 8.5 Open the file mbox-short.txt and read it line by line. When you
# find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in
# the line (i.e. the entire address of the person who sent the message). Then
# print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

# Read input file
fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)

# Initialize useful variables
count = 0

# Iterate through each line and search for "From " to print out
for line in fh:
    if "From " not in line:
        continue
    email = line.split()
    print(email[1])
    count = count + 1

# Print desired output
print("There were", count, "lines in the file with From as the first word")
