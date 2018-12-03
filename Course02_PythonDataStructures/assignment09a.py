# Assignment 09a - Chapter 9
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 2 - Python Data Structures

# Problem: 9.4 Write a program to read through the mbox-short.txt and figure out
# who has the sent the greatest number of mail messages. The program looks for
# 'From ' lines and takes the second word of those lines as the person who sent
# the mail. The program creates a Python dictionary that maps the sender's mail
# address to a count of the number of times they appear in the file. After the
# dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer.

# Read input file
inputFile = input("Enter file:")
if len(inputFile) < 1:
    inputFile = "mbox-short.txt"
fileHandle = open(inputFile)

# Initialize useful variables
largestCount = None
largestWord = None
countDict = dict()

# Evaluate each line for email addresses and tally them up
for line in fileHandle:
    if "From: " not in line:
        continue
    textArray = line.split()
    countDict[textArray[1]] = countDict.get(textArray[1],0) + 1

# Iterate through the dictionary to find the one with the largest occurence
for key,value in countDict.items():
    if largestCount is None or value > largestCount:
        largestWord = key
        largestCount = value

# Print desired output
print(largestWord, largestCount)
