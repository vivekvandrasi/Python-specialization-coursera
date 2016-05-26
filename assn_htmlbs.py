import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('span')
sumtag = 0
for tag in tags:
    sumtag = sumtag + int(tag.text)
print sumtag
