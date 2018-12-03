# Assignment 10 - Chapter 10
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 2 - Python Data Structures

# Problem: 10.2 Write a program to read through the mbox-short.txt and figure out
# the distribution by hour of the day for each of the messages. You can pull the
# hour out from the 'From ' line by finding the time and then splitting the
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
# sorted by hour as shown below.

# Read input file
inputFile = input("Enter file:")
if len(inputFile) < 1:
    inputFile = "mbox-short.txt"
fileHandle = open(inputFile)

# Initialize useful variables
hourList = dict()

# Scan each line for the "From " text and retrieve the hour sent
for line in fileHandle:
    if "From " not in line:
        continue
    textArray = line.split()
    sentHour = textArray[5].split(':')[0]
    hourList[sentHour] = hourList.get(sentHour, 0) + 1

# Print desired output
for k,v in sorted(hourList.items()):
    print(k,v)
