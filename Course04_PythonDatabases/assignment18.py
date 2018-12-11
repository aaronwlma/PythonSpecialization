# Assignment 18
# For University of Michigan's Coursera Specialization "Python for Everybody"
# Course 4 - Using Databases with Python

# Problem: Musical Track Database
# This application will read an iTunes export file in XML and produce a properly
# normalized database with this structure:

# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );
#
# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY
#         AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );

# If you run the program multiple times in testing or with different files, make
# sure to empty out the data before each run.

# You can use this code as a starting point for your application:
# http://www.py4e.com/code3/tracks.zip. The ZIP file contains the Library.xml
# file to be used for this assignment. You can export your own tracks from
# iTunes and create a database, but for the database that you turn in for this
# assignment, only use the Library.xml data that is provided.

# To grade this assignment, the program will run a query like this on your
# uploaded database and look for the data it expects to see:

# SELECT Track.title, Artist.name, Album.title, Genre.name
#     FROM Track JOIN Genre JOIN Album JOIN Artist
#     ON Track.genre_id = Genre.ID and Track.album_id = Album.id
#         AND Album.artist_id = Artist.id
#     ORDER BY Artist.name LIMIT 3

# The expected result of the modified query on your database is: (shown here as
# a simple HTML table with titles)

# Track	Artist	Album	Genre
# Chase the Ace	AC/DC	Who Made Who	Rock
# D.T.	AC/DC	Who Made Who	Rock
# For Those About To Rock (We Salute You)	AC/DC	Who Made Who	Rock

# Import Relevant Libraries
import xml.etree.ElementTree as ET
import sqlite3

# Create sqlite file and initialize database cursor
conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Make sure tables created are new
cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Genre;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name  TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title  TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title  TEXT UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len  INTEGER, rating INTEGER, count INTEGER
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name  TEXT UNIQUE
    );
''')

# Read input file
fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'Library.xml'
fh = open(fname)

# Function to retrieve text from each key
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

# Parse XML for relevant information and print the number of entries
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

# Main body to retrieve info and create SQLite database from it
for entry in all:
    # Check if there is actually a track
    if (lookup(entry, 'Track ID') is None):
        continue

    # Grab the info in the entry and assign it to variables to store
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    # Check if any of the table values don't exist, if they don't, skip it
    if name is None or artist is None or album is None or genre is None:
        continue

    # Print statement for troubleshooting
    print(name, artist, album, count, rating, length, genre)

    # Create Artist table
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',
        (artist, ))
    # Create foreign key for artist to put in Album
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist, ))
    artist_id = cur.fetchone()[0]

    # Create Album table
    cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )',
        (album, artist_id))
    # Create foreign key for album to put in track
    cur.execute('SELECT id FROM Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]

    # Create Genre table
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)',
        (genre, ))
    cur.execute('SELECT id FROM Genre WHERE name = ?', (genre, ))
    genre_id = cur.fetchone()[0]

    # Create Track table
    cur.execute('INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES ( ?, ?, ?, ?, ?, ?)',
        (name, album_id, genre_id, length, rating, count))

    # Push changes
    conn.commit()

# Close cursor
cur.close()
