# Assignment 13
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 3 - Using Python to Access Web Data

# Problem:

# Exploring the HyperText Transport Protocol

# You are to retrieve the following document using the HTTP protocol in a way
# that you can examine the HTTP Response headers.

# http://data.pr4e.org/intro-short.txt

# There are three ways that you might retrieve this web page and look at the
# response headers:

# Preferred: Modify the socket1.py program to retrieve the above URL and print
# out the headers and data. Make sure to change the code to retrieve the above
# URL - the values are different for each URL.

# Open the URL in a web browser with a developer console or FireBug and
# manually examine the headers that are returned.

# Use the telnet program as shown in lecture to retrieve the headers and
# content.

# Enter the header values in each of the fields below and press "Submit".

# Import relevant libraries
import socket

# Open a socket and retrieve desired web URL
# Initialize a socket that opens to the Internet
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the host on port 80
mySocket.connect(('data.pr4e.org', 80))
# Command GET URL using HTTP 1.0 and then hit enter twice, then convert from
# unicode to UTF-9 text format
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# Send predefined command
mySocket.send(cmd)

# Receive web server data and interpret
while True:
    data = mySocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# Once all data is received, close socket
mySocket.close()

# Telnet command to get the same information
# telnet HOST PORT
# telnet data.pr4e.org 80
# COMMAND URL PROTOCOL
# GET http://data.pr4e.org/intro-short.txt HTTP/1.0
