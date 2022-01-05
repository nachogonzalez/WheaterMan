import json
import os
import logging
import datetime
import requests
from utils import loggingInitialization
from utils import loadJSONfile
from utils import getCitiesNumber
from utils import getCitiesList
from utils import getNumberOfCountries
from utils import getCityWeather

# Initialization of the logging system
loggingInitialization()

data = loadJSONfile('data/city.list.json')
logging.info("Data structure loaded succesfully from JSON file")

citiesNumber = getCitiesNumber(data)
logging.info("Number of cities in the JSON file: " + str(citiesNumber))

citiesList = getCitiesList(data)
logging.info("List of cities obtained")

print("Number of different countries: " + str(getNumberOfCountries(data)))

cityName = "Santander"
getCityWeather(cityName)
