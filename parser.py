import urllib2

response = urllib2.urlopen('http://www.corvallis-bus.appspot.com/arrivals?stops=13713')
html = response.read()

print html