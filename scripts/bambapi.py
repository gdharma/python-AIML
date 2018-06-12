#!/usr/bin/env python
from sys import argv

import requests
import urllib3
from jira import JIRA

from scripts.ConfigParser import getConfig

jiraUserName=getConfig("Anthem","user")
jiraPassword=getConfig("Anthem","password")

# jql=input("Enter the text")
bambooUrl="https://bamboo.anthem.com"

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


url = bambooUrl+'/rest/api/latest/queue/OCP-THUNDERBIRDNEW'
# bambooUrl1=bambooUrl+'/rest/api/latest/info'
headers = {'Content-Type': 'application/json','Accepts': 'application/json'}

    # create page
    # [USERNAME], i.e.: admin
    # [PASSWORD], i.e.: admin
urllib3.disable_warnings (urllib3.exceptions.InsecureRequestWarning)
r = requests.post(url, headers=headers, auth=(jiraUserName, jiraPassword),verify=False)
print (r.status_code)
print (r.text)



# jiraPython="https://community.atlassian.com/t5/Jira-Core-questions/List-all-the-issues-of-a-project-with-JIRA-Python/qaq-p/350521"
# sec="https://stackoverflow.com/questions/45104975/issue-in-connecting-with-jira-python"
# smapleurl="https://jira.atlassian.com/issues/?filter=-5&jql=reporter%20in%20(vic)%20AND%20text%20~%20%22text%22%20order%20by%20priority%20DESC%2Cupdated%20DESC"
# jiraPython="https://community.atlassian.com/t5/Jira-questions/How-do-I-access-the-hosted-Jira-API-via-python/qaq-p/505632"

# def main():
#   print issue.fields.project.key
#    print issue.fields.issuetype.name
#    print issue.fields.reporter.displayName
#    print issue.fields.summary
#    print issue.fields.project.id

#
# if __name__== "__main__" :
#      main()