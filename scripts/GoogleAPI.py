import webbrowser
from sys import argv

import sys

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# searchquery="ipl final 2018"
# searchquery=argv[1].upper()
print("Opening google")
searchquery=" ".join(sys.argv[1:])
googleURL='https://www.google.com.sg/search?q="'+searchquery+'"'
webbrowser.get(chrome_path).open(googleURL)