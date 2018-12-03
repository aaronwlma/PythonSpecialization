# Assignment 08a - Chapter 8
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 2 - Python Data Structures

# Problem: 8.4 Open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split() method. The program
# should build a list of words. For each word on each line check to see if the
# word is already in the list and if not append it to the list. When the program
# completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

# Read input file
fname = input("Enter file name: ")
fh = open(fname)

# Initialize empty list
lst = list()

# Read the file, split between spaces, and sort
wordsArray = fh.read().split()
wordsArray.sort()

# Remove duplicate words and add to initialized list
for word in wordsArray:
    if word in lst:
        continue
    lst.append(word)
    
# Sort words and print
print(lst)
