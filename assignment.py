#Part 1: Look in the CSV file, and find the station code for Seattle.
#Use this station code to select all the measurements belonging to it from the JSON data
#Sum all the measurement for that location for each month (i.e.  create a list with the total monthly precipitation).
#Save the results to a JSON file
import json
import csv

seattle_precipitation = [0]*12 #create an empty list with 12 0s for the 12 months
seattle_code = "GHCND:US1WAKG0038"

'''
with open('stations.csv', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    seattle_code = reader[2][2]
'''

#for all of the dictionary entries with the station code for seattle, select the value of 'value' for each;
# also select the value of 'date' for each and sum the values for 'value' for each month
with open ('precipitation.json', encoding='utf-8-sig') as file:
    measurements = json.load(file)
    for measurement in measurements:
        if measurement['station'] == seattle_code:
            # Find value of rainfall
            rainfall = measurement["value"]
            # Find month
            month = int(measurement["date"].split('-')[1])
            # Add value to the right index of seattle_precipitation
            seattle_precipitation[month-1] += rainfall

print(seattle_precipitation)

with open('seattle.json', 'w') as file: 
    json.dump(seattle_precipitation, file)


#Part 2: Calculate the sum of the precipitation over the whole year
#Calculate the relative precipitation per month (percentage compared to the precipitation over the whole year
year_precipitation = sum(seattle_precipitation[0:])

relative_precipitation = [0]*12
for i in range(12):
    relative_precipitation[i] = (seattle_precipitation[i]/year_precipitation)*100
    
#relative_precipitation_jan = (seattle_precipitation[0]/year_precipitation)*100
print(relative_precipitation)
#relative_precipitation[month-1] = seattle_precipitation/year_precipitation
