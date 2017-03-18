ex. 1

from urllib2 import Request, urlopen, URLError

request = Request('http://placekitten.com/')

try:
	response = urlopen(request)
	kittens = response.read()
	print kittens[559:1000]
except URLError, e:
    print 'No kittez. Got an error code:', e


ex.2

from urllib2 import urlopen

kittens = urlopen('http://placekitten.com/200/300')

f = open('kittens.jpg', 'wb')
f.write(kittens.read())
f.close()


ex.3

from urllib2 import urlopen

# Open http://placekitten.com/ for reading on line 4!
kittens = urlopen("http://placekitten.com/")
response = kittens.read()
body = response[559:1000]

# Add your 'print' statement here!
print(body)


ex. 4

import requests

# Make a GET request here and assign the result to kittens:
kittens = requests.get("http://placekitten.com")

print kittens.text[559:1000]