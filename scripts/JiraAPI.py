#!/usr/bin/env python
import urllib.request
import json
import datetime
from sys import argv

# ZIPCODE="Chennai"
# day="SUNDAY"
import aiml
BRAIN_FILE="brain.dump"
jql=input("Enter the text")
jql=jql.replace(" ","%20")
jqlURl='https://dharmag.atlassian.net/rest/api/2/search?jql=text%20~%20%22'+jql+'%22'

try:
    JSONresponse=urllib.request.urlopen(jqlURl).read()
    weatherReport=json.loads(JSONresponse)
    minweatherReport=weatherReport['main']['temp_min']
    maxweatherReport = weatherReport['main']['temp_max']
    mainweatherReport=weatherReport['weather'][0]['description']
  # if day == 0:
    print("Today, it will be",mainweatherReport,"with a high of",minweatherReport,"degrees and a low of",minweatherReport,"degrees.")
  # else:
except:
  print("Something went wrong")

smapleurl="https://jira.atlassian.com/issues/?filter=-5&jql=reporter%20in%20(vic)%20AND%20text%20~%20%22text%22%20order%20by%20priority%20DESC%2Cupdated%20DESC"
jiraPython="https://community.atlassian.com/t5/Jira-questions/How-do-I-access-the-hosted-Jira-API-via-python/qaq-p/505632"

# def main():
#
#    options = {'server': jiraURL}
#    jira = JIRA(options, basic_auth=(jiraUserName, jiraPassword))
#    issue = jira.issue('ESS-138581')
#
#    print issue.fields.project.key
#    print issue.fields.issuetype.name
#    print issue.fields.reporter.displayName
#    print issue.fields.summary
#    print issue.fields.project.id
#
#
# if __name__== "__main__" :
#      main()