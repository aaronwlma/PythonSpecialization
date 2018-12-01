# Assignment 07a - Chapter 7
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 2 - Python Data Structures

# Problem: 7.2 Write a program that prompts for a file name, then opens that file and
# reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and
# compute the average of those values and produce an output as shown below. Do not use
# the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you
# are testing below enter mbox-short.txt as the file name.

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

# Initialize useful variables
count = 0
runningTotal = 0

# For-loop that parses for the confidence values, and tallies up the total and count
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    runningTotal = runningTotal + float(line.lstrip('X-DSPAM-Confidence: ').rstrip())

# Calculate the average based on the retrieved values
average = runningTotal / count

# Print the desired output
print("Average spam confidence:", average)
