#!/usr/bin/env python
from sys import argv

import urllib3
from jira import JIRA

from scripts.ConfigParser import getConfig

jiraUserName=getConfig("Anthem","user")
jiraPassword=getConfig("Anthem","password")

# jql=input("Enter the text")
jiraURL="https://jira.anthem.com"
# jql= argv[1].upper()
jql1='issueType=Story AND assignee =AF25454'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
options = {'server': jiraURL,'verify': False}


rootnn_dict = {'project' : { 'id': '14253' },
    'summary' : 'Test Execution',
    'description' : 'Test Execution',
    'issuetype' : { 'name' : 'Sub-task' },
    'assignee' : {'name':'AF25454'},
    'timetracking':{'originalEstimate':'2d'},
    'parent' : { 'id' : 'OCP-88367'},
    }

# try:
jira = JIRA (options, basic_auth=(jiraUserName, jiraPassword))
issues = jira.search_issues (jql1)
# subtask=jira.create_issue(rootnn_dict)
for issue in issues:
    print(issue.key)

# except:
#     print("Something went wrong")
