import os
import time

print("Downloading.....")
time.sleep(1)
print("Please be patient...")
time.sleep(1)
print("This may take a while...")

link="http://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
os.system("wget http://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip")

print("Donwloaded!")
print("unzipping...")

os.system("unzip vosk-model-small-en-us-0.15.zip")

os.system("mv vosk-model-small-en-us-0.15 model")
