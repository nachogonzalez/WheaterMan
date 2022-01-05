import json
import os
import logging
import datetime
import requests

# Hardcoded variables (to be extracted into other dedicated module)
LOG_FILE = "logs/WheaterMan.log"
API_KEY = "33374ad19b134b3003cb38b0851e2094"

# ****** Log configuration and initialization ******

def loggingInitialization():
	file = open(LOG_FILE, "w")
	timestamp = datetime.datetime.now()
	file.close()
	logging.basicConfig(
		filename = LOG_FILE, 
		encoding = 'utf-8', 
		level = logging.INFO, 
		format='%(asctime)s %(levelname)-8s %(message)s',
		datefmt='%Y-%m-%d %H:%M:%S')
	logging.info("Logging system initialized \n")
	
# ****** JSON parsing ******

def loadJSONfile(jsonfile):
	# We use the “latin-1” encoding to map byte values directly to the first 256 Unicode code points
	with open('data/city.list.json', encoding='latin-1') as f:
		data = json.load(f)
	f.close()
	return data
	
def getCitiesList(data):
	citiesList = []
	i = 0
	for item in data:
		element = data[i]
		citiesList.append(element["name"])
		i = i + 1
	return citiesList
	
def getCountriesList(data):
	countriesList = []
	i = 0
	for item in data:
		element = data[i]
		country = element["country"]
		if country not in countriesList:
			countriesList.append(country)
		i = i + 1
	return countriesList
	
def getNumberOfCountries(data):
	countriesList = getCountriesList(data)
	return len(countriesList)
			
def getCitiesNumber(data):
	return len(data)
	
def getCityWeather(city):
	response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY)
	logging.info("OpenWeather API response code: " + str(response.status_code))
	logging.info("OpenWeather API response JSON:\n" + json.dumps(response.json(), indent=4, sort_keys=True))