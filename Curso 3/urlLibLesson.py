import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

data = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in data:
    print(line.decode().strip())

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for i in fhand:
    words = i.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter --')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

#Retrieve the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))