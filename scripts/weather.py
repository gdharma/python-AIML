#!/usr/bin/env python
import urllib.request
import json
import datetime
from sys import argv

# ZIPCODE="Chennai"
# day="SUNDAY"
import aiml

# ZIPCODE=kernel.getPredicate("weather")
ZIPCODE=argv[1].upper()
# ZIPCODE= 'Chennai'
try:
    JSONresponse=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ZIPCODE+'&APPID=7e453708f8679396e13bbd415ec2e132&units=metric').read()
    str_response = JSONresponse.decode ('utf-8')
    weatherReport=json.loads(str_response)
    minweatherReport=weatherReport['main']['temp_min']
    maxweatherReport = weatherReport['main']['temp_max']
    mainweatherReport=weatherReport['weather'][0]['description']
    print("Today, it will be",mainweatherReport,"with a high of",minweatherReport,"degrees and a low of",minweatherReport,"degrees.")
except:
    print("Something went wrong")
