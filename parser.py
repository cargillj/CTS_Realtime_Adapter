import urllib2
import json

#this calls the stop IDs for processing and saving into a list
response = urllib2.urlopen('http://www.corvallis-bus.appspot.com/stops')
data = response.read()

#list of bus ids
id_list = []							

#parse for id info
for i in range(0, len(data)):
	if data[i:(i+5)] == '"ID":':				
		id_list.append(data[(i+5):(i+10)])		

#an array for storing the times of each route 
timesArray = []									

#text file containing the information in gtfs format 
gtfsUpdateFile = open("gtfsUpdateFile.txt", "w")

for iterator in range(0, 5):
	response = urllib2.urlopen('http://www.corvallis-bus.appspot.com/arrivals?stops=' + id_list[iterator])
	apiresponse = response.read()	
	timesArray.append(apiresponse)

for i in range(0, len(timesArray)): 
	 if timesArray[i:(i+14)] == '"Expected":':				
		id_list.append(data[(i+5):(i+10)])	

print timesArray[0]
