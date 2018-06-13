

import requests
import sys
import urllib3
from scripts.ConfigParser import getConfig

jiraUserName=getConfig("Anthem","user")
jiraPassword=getConfig("Anthem","password")
planquery=" ".join(sys.argv[1:]).upper()
if ("THUNDERBIRD" and "SIT5" and "SMOKE" in planquery):
    bambooUrl="https://bamboo.anthem.com"
    url = bambooUrl+'/rest/api/latest/queue/OCP-THUNDERBIRDNEW'
    headers = {'Content-Type': 'application/json','Accepts': 'application/json'}
    urllib3.disable_warnings (urllib3.exceptions.InsecureRequestWarning)
    r = requests.post(url, headers=headers, auth=(jiraUserName, jiraPassword),verify=False)
    if(r.status_code==200):
        print("Triggered")
    else:
        print ("Something Wrong")

