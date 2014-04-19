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

for iterator in range(0, 10):
	response = urllib2.urlopen('http://www.corvallis-bus.appspot.com/arrivals?stops=' + id_list[iterator])
	apiresponse = response.read()	
	timesArray.append(apiresponse)

bus_data = [[], [], []]

for i in range(0, len(timesArray)): 
	bus_data[0].append(id_list[i])
	bus_data[1].append(timesArray[i][32:37])
	bus_data[2].append(timesArray[i][81:86])

print timesArray[9]
#{"10090":[{"Expected":"19 Apr 14 15:52 -0700","Route":"3","Scheduled":"19 Apr 14 15:52 -0700"}