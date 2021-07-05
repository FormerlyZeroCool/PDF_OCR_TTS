import os
import sys
from gtts import gTTS
import pyttsx3
import vlc
import time
voice_driver = "nsss"
engine = pyttsx3.init(driverName = voice_driver)
def say(text, rate = 1):
    engine.setProperty('rate', int(200*rate))
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.1*(1/rate))
filepath = ''
playback_rate = 1
startingLine = 0
print("command line parameters")
print("<filepath> <playback rate> <line of text to start on>")
if(len(sys.argv)>1):
    filepath = sys.argv[1]
    if(len(sys.argv) > 2):
        playback_rate = float(sys.argv[2])
        if(len(sys.argv) > 3):
            startingLine = int(sys.argv[3])
else:
    filepath = "output.txt"

file = open(filepath,'r')
data = file.read()
if(startingLine < 0):
    startingLine = 0
dataList = data.replace('-',' ').split('.')
lines = dataList[startingLine:]
sentenceNo = startingLine
lineNo = 0
previousLines = dataList[0:startingLine]

for line in previousLines:
    lineNo += line.count("\n")
for line in lines:
    if(len(line)>1):
        print("Sentence number:", sentenceNo,": remaining", len(lines) - sentenceNo)
        splitlines = line.split('\n')
        for indivLine in splitlines:
            if(len(indivLine) > 1):
                print(lineNo,":",indivLine)
                lineNo += 1
        say(line, playback_rate)
        print('')
        sentenceNo += 1
        #input()

