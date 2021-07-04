import speech_recognition as sr
import os
import pywhatkit as pwk

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

r = sr.Recognizer()
data = sr.AudioFile('speech.wav')
with data as source:
    audio = r.record(source)
    text = r.recognize_google(audio, language="en-IN")
    print(text)

if "Alexa" in text:
    text.replace("Alexa", "")

if "open" in text:
    if "Chrome" in text:
        os.system("python open.py chrome")
if "play" in text:
        print("play in text")
        driver = webdriver.Firefox(executable_path="/home/garuda/Github projects/Virtual-assistant/geckodriver")
        driver.implicitly_wait(5)

        # Let's create a list of terms to search for and an empty list for links
        search_terms = [text]
        links = []

        for term in search_terms:
            # Open YouTube page for each search term
            driver.get('https://www.youtube.com/results?search_query={}'.format(term))
            # Find a first webelement with video thumbnail on the page
            link_webelement = driver.find_element(By.CSS_SELECTOR, 'div#contents ytd-item-section-renderer>div#contents a#thumbnail')
            # Grab webelement's href, this is your link, and store in a list of links:
            links += [link_webelement.get_attribute('href')]
else:
    print("no useful commands found")    


print(links)
driver.quit()
os.system("google-chrome-stable "+links[0])

print("2 done")
