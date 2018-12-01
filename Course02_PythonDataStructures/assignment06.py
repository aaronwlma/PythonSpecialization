# Assignment 06 - Chapter 6
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 2 - Python Data Structures

# Problem: 6.5 Write code using find() and string slicing (see section 6.10) to
# extract the number at the end of the line below. Convert the extracted value
# to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
index = text.find('0.8475')
print(float(text[index:index + 6]))
