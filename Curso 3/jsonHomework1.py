import json
import urllib.error, urllib.parse, urllib.request

#url = http://py4e-data.dr-chuck.net/comments_843088.json
url = input('Enter-- ')
data = urllib.request.urlopen(url).read()

info = json.loads(data)
print('User count:', len(info))
count = 0
for item in info['comments']:
    count += int(item['count'])
print(count)