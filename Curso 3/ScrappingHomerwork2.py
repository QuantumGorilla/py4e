import urllib.error, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import ssl

#url = http://py4e-data.dr-chuck.net/known_by_Beraka.html
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
position = int(input('Position of the href: ')) - 1
count = int(input('How many pages you wanna navigate: '))
links = []
tags = soup('a')

for i in range(count):
    link = tags[position].get('href', None)
    print("I'm in:",link)
    links.append(tags[position].contents[0])
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    
print(links)