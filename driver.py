import sys
import os
import time
if len(sys.argv) < 2:
    print("error missing filepath to pdf") 
    exit(1)
pdfPath = sys.argv[1]

if sys.platform == "win32":
    pathsep = "\\"
else:
    pathsep = "/"
fileName = pdfPath.split(pathsep)
fileName = fileName[len(fileName) - 1]
fileName = fileName.split('.')[0] + '.txt'
print(fileName)
if(not(os.path.exists(fileName))):
    os.system('python3 pdf_ocr.py ' + pdfPath + ' ' + fileName)
    print("Done generating text file using OCR")
else:
    print("Skipping text file conversion using OCR file already detected")
playback_rate = '1'
startingLine = '0'
if(len(sys.argv) > 2):
    playback_rate = (sys.argv[2])
    if(len(sys.argv) > 3):
        startingLine = (sys.argv[3])
os.system('python3 read.py ' + fileName + ' ' + playback_rate + ' ' + startingLine)