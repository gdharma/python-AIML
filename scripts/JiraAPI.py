#!/usr/bin/env python
import urllib.request
import urllib3
import json
from jira import JIRA
import datetime
from sys import argv

# ZIPCODE="Chennai"
# day="SUNDAY"
import aiml
BRAIN_FILE="brain.dump"
# jiraUserName="dfus@live.com"
jiraUserName="gdharma"
jiraPassword="Apr@2018"
# jql=input("Enter the text")
jiraURL="https://jira.atlassian.com"
# jql=jql.replace(" ","%20")
jqlURl='https://jira.atlassian.com/rest/api/2/search?jql=issuetype%20%3D%20Bug%20AND%20reporter%20%3D%20"Ahmad%20Faridi"'
jql='issuetype%20%3D%20Bug%20AND%20reporter%20%3D"Ahmad%20Faridi"'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
options = {'server': jiraURL,'verify': False}
jira = JIRA(options, basic_auth=(jiraUserName, jiraPassword))
# issue = jira.issue('ESS-138581')

issues=jira.search_issues(jql)

#
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
jiraPython="https://community.atlassian.com/t5/Jira-Core-questions/List-all-the-issues-of-a-project-with-JIRA-Python/qaq-p/350521"
sec="https://stackoverflow.com/questions/45104975/issue-in-connecting-with-jira-python"
smapleurl="https://jira.atlassian.com/issues/?filter=-5&jql=reporter%20in%20(vic)%20AND%20text%20~%20%22text%22%20order%20by%20priority%20DESC%2Cupdated%20DESC"
jiraPython="https://community.atlassian.com/t5/Jira-questions/How-do-I-access-the-hosted-Jira-API-via-python/qaq-p/505632"

# def main():
#   print issue.fields.project.key
#    print issue.fields.issuetype.name
#    print issue.fields.reporter.displayName
#    print issue.fields.summary
#    print issue.fields.project.id

#
# if __name__== "__main__" :
#      main()