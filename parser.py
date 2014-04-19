import urllib2

#this calls the stop IDs for processing and saving into a list
response = urllib2.urlopen('http://www.corvallis-bus.appspot.com/stops')
data = response.read()

#list of stop ids
stop_list = []							

#parse for id info
for i in range(0, len(data)):
	if data[i:(i+5)] == '"ID":':				
		stop_list.append(data[(i+5):(i+10)])		

#an array for storing the times of each route 
timesArray = []									

#text file containing the information in gtfs format 
gtfsUpdateFile = open("gtfsUpdateFile.txt", "w")

for iterator in range(0, 10):
	response = urllib2.urlopen('http://www.corvallis-bus.appspot.com/arrivals?stops=' + stop_list[iterator])
	apiresponse = response.read()	
	timesArray.append(apiresponse)

#2-d array holding the stop_id and arrival times
stop_data = [[], [], []]

for i in range(0, len(timesArray)):
	print timesArray[i]

#{"10090":[{"Expected":"19 Apr 14 15:52 -0700","Route":"3","Scheduled":"19 Apr 14 15:52 -0700"}