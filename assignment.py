#Part 1: Look in the CSV file, and find the station code for Seattle.
#Use this station code to select all the measurements belonging to it from the JSON data
#Sum all the measurement for that location for each month (i.e.  create a list with the total monthly precipitation).Save the results to a JSON file
import csv
import json

open('stations.csv')
open('precipitation.json')

seattle_precipitation = [] #create an empty list
station_code = "GHCND:US1WAKG0038"

with open ('precipitation.json', encoding='utf8') as file:
    for line in file: #for all the lines in this file
        if station_code in file:
            print(station_code)
            

with open('seattle.json', 'w') as file: #w = writing; r = reading (read-only file); output is in another file named 'output.json'
    json.dump(seattle_precipitation, file)

#Part 2: Calculate the sum of the precipitation over the whole year1
#Calculate the relative precipitation per month (percentage compared tothe precipitation over the whole year)