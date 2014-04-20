import urllib2

# converts strings '12:00' to ints for comparison
def strTimeToInt(time):
	hours = int(time[0:2]) * 60
	mins = int(time[3:5])
	result = hours + mins
	return result


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

for iterator in range(0, len(stop_list)):
	response = urllib2.urlopen('http://www.corvallis-bus.appspot.com/arrivals?stops=' + stop_list[iterator])
	apiresponse = response.read()	
	timesArray.append(apiresponse)

#2-D array.  first element holds stop ids.  Second holds scheduled
#and estimated times, and routes.
bus_data = [[], []]

for i in range(0, len(stop_list)):
	bus_data[0].append(stop_list[i])

	stop_times = [[], [], []]
	for j in range(0, len(timesArray[i])):
		
		route = ''

		if(timesArray[i][j:(j+8)] == 'Expected'):
			stop_times[0].append(strTimeToInt(timesArray[i][(j+21):(j+26)]))
		elif(timesArray[i][(j):(j+5)] == 'Route'):
			for k in range((j+8), len(timesArray[i])):
				if(timesArray[i][k] != '"'):
					route += timesArray[i][k]
				else:
					break
			stop_times[1].append(route)
		elif(timesArray[i][j:(j+9)] == 'Scheduled'):
			stop_times[2].append(strTimeToInt(timesArray[i][(j+22):(j+27)]))

	bus_data[1].append(stop_times)

for i in range(0, len(stop_list)):
	print bus_data[0][i]
	print bus_data[1][i]

#{"10090":[{"Expected":"19 Apr 14 15:52 -0700","Route":"3","Scheduled":"19 Apr 14 15:52 -0700"}