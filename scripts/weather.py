#!/usr/bin/env python
import urllib.request
import json
import datetime
from sys import argv

# ZIPCODE="Chennai"
# day="SUNDAY"
import aiml

# ZIPCODE=kernel.getPredicate("weather")
# ZIPCODE=argv[1].upper()
# ZIPCODE= 'Chennai'
# ZIPCODE=input("What location?")
def weather(ZIPCODE):
    try:
        JSONresponse=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ZIPCODE+'&APPID=7e453708f8679396e13bbd415ec2e132&units=metric').read()
        str_response = JSONresponse.decode ('utf-8')
        weaterReport=json.loads(str_response)
        minweatherReport=weaterReport['main']['temp_min']
        maxweatherReport = weaterReport['main']['temp_max']
        mainweatherReport=weaterReport['weather'][0]['description']
        print("Today, it will be",mainweatherReport,"with a high of",maxweatherReport,"degrees and a low of",minweatherReport,"degrees.")
        return mainweatherReport
    except:
        print("Something went wrong")



# weather(ZIPCODE)