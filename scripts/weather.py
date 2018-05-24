#!/usr/bin/env python
import urllib.request
import json
import datetime
from sys import argv

# ZIPCODE="Chennai"
# day="SUNDAY"
import aiml
BRAIN_FILE="brain.dump"
kernel = aiml.Kernel()
ZIPCODE=kernel.getPredicate("location")
ZIPCODE= argv[1].upper()

try:
#   if day == 'TODAY':
#     day = 0
#   elif day == 'TOMORROW':
#     day = 1
#   else:
#     weekday = (datetime.datetime.today().isoweekday())%7
#     week  = ['SUNDAY',
# 	      'MONDAY',
# 	      'TUESDAY',
# 	      'WEDNESDAY',
# 	      'THURSDAY',
# 	      'FRIDAY',
# 	      'SATURDAY']
#     day = week.index(day)+weekday+1
    
    JSONresponse=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ZIPCODE+'&APPID=7e453708f8679396e13bbd415ec2e132&units=metric').read()
    weatherReport=json.loads(JSONresponse)
    minweatherReport=weatherReport['main']['temp_min']
    maxweatherReport = weatherReport['main']['temp_max']
    mainweatherReport=weatherReport['weather'][0]['description']
  # if day == 0:
    print("Today, it will be",mainweatherReport,"with a high of",minweatherReport,"degrees and a low of",minweatherReport,"degrees.")
  # else:
except:
  print("Something went wrong")
