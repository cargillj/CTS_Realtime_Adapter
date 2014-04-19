import urllib2
import json

response = urllib2.urlopen('http://www.corvallis-bus.appspot.com/stops')
data = response.read()

id_list = []							#list of bus ids

for i in range(0, len(data)):
	if data[i:(i+5)] == '"ID":':				#parse for idf info
		id_list.append(data[(i+5):(i+10)])		

print id_list[0]
