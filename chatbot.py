#!/usr/bin/python3
import os
import aiml
# from gtts import gTTS
import time

BRAIN_FILE="brain.dump"

k = aiml.Kernel()


# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.
# if os.path.exists(BRAIN_FILE):
#     print("Loading from brain file: " + BRAIN_FILE)
#     k.loadBrain(BRAIN_FILE)
# else:
print("Parsing aiml files")
k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
print("Saving brain file: " + BRAIN_FILE)
k.saveBrain(BRAIN_FILE)
k.learn("alice.aiml")

# Endless loop which passes the input to the bot and prints
# its response
while True:
    input_text = input("> ")
    response = k.respond(input_text)
    language = 'en'
    # myobj = gTTS(text=response, lang=language, slow=False)
    # myobj.save("welcome.mp3")

    # Playing the converted file
    # os.system("welcome.mp3")
    print(response)
