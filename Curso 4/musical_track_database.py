import sqlite3
import xml.etree.ElementTree as ET
conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;''') 

cur.executescript('''CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')  

file = input('Enter file name (XML Format): ')
if len(file) < 1: 
    fh = open('Library.xml')
else:
    fh = open(file) #Must be in XML format
tree = ET.fromstring(fh.read())
dicts = tree.findall('./dict/dict/dict')

def lookup(pare, aim):
    flag = False
    for child in pare:
        if flag:
            return child.text
        if child.tag == 'key' and child.text == aim:
            flag = True
    return None

# Track ID   Name    Artist     Album   Play Count  Rating  Total Time
for entry in dicts:
    if(lookup(entry, 'Track ID') is None):  continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')
    if name is None or artist is None or album is None or genre is None:
        continue
    print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist(name) VALUES(?)''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]   # 查询返回的是数组
    cur.execute('INSERT OR IGNORE INTO Genre(name) VALUES(?)', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
    genre_id = cur.fetchone()[0]
    cur.execute('INSERT OR IGNORE INTO Album(artist_id, title) VALUES(?, ?)',(artist_id, album))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    album_id = cur.fetchone()[0]
    

    cur.execute('''INSERT OR REPLACE INTO Track(title, album_id, genre_id, len, rating, count) 
    VALUES(?, ?, ?, ?, ?, ?)''',(name, album_id, genre_id, length, rating, count))
    
conn.commit()
cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')
res = cur.fetchall()
for line in res:
    print(line)
cur.close()