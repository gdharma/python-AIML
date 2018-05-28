#!/usr/bin/env python
from sys import argv

import urllib3
from jira import JIRA

jiraUserName="AF25454"
jiraPassword="May@2018"
# jql=input("Enter the text")
jiraURL="https://jira.anthem.com"
jql= argv[1].upper()
# jql1='issueType=Story AND assignee =AF25454'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
options = {'server': jiraURL,'verify': False}

try:
    jira = JIRA (options, basic_auth=(jiraUserName, jiraPassword))
    issues = jira.search_issues (jql)
    for issue in issues:
        print(issue.key)

except:
  print("Something went wrong")


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