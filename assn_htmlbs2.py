import urllib 
import re
from BeautifulSoup import *

url = raw_input('Enter URL: ')
count = int(raw_input('Enter count: '))
position = int(raw_input('Enter position: '))

print "Retreiving: ", url

for i in range(count):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    url = str(soup('a')[position-1]).split('"')[1]
    print "Retreiving: ", url
    
print re.findall('known_by_(.+).html',url)[0]    
