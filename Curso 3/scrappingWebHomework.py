from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
sum = 0
for tag in tags:
    # Look at the parts of a tag
    numbers = re.findall('[0-9]+',str(tag))
    for number in numbers:
        sum += int(number)
print(sum)