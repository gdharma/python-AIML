import configparser
import os

def getConfig(Key,value):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    workingdir=ROOT_DIR.replace("scripts","Config")
    config = configparser.ConfigParser()
    config.read(workingdir+"\\"+'Config.ini')   # -> "/path/name/"
    value=config[Key][value]
    return value

getConfig("Anthem","user")
