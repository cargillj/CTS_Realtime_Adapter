import urllib2

stops = ['1', '2', '3', '4', '5', '6', '7']

response = urllib2.urlopen('http://www.corvallis-bus.appspot.com/arrivals?stops={stopID}').format(iterator)
apiresponse = response.read()
timesarray = apiresponse.split("Expected")
savefile = open("savefile.txt", "w")
savefile.write(timesarray[4])

print len(timesarray)
