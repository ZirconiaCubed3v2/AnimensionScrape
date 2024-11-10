from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

found = False
epList = open("episodeslist.txt", 'w')
brave = "/usr/bin/brave"
driverpath = "/usr/bin/chromedriver"
service = Service(driverpath)
options = Options()
options.binary_location = brave
options.add_argument("--remote-debugging-port=9224")
browser = webdriver.Chrome(service=service, options=options)

fileNameFormat = "" # put the filename format for the downloads here, first %s is episode number, second %s is resolution (1080p, 720p, 480p, etc)
animensionURL = "" # put the url for the show's page here

def formatString(string):
    return string.lower().replace("download ", "").replace(" - mp4)", "")[1:]

browser.get(animensionURL)
while (found == False):
    try:
        buttons = browser.find_elements(By.CLASS_NAME, "btn.btn-sm.btn-go2")
        found = True
    except Exception:
        pass
found = False
epNum = len(buttons)
for button in buttons:
    button.click()
    while (found == False):
        try:
            browser.find_elements(By.CLASS_NAME, "official-button")[-1].click()
            found = True
        except Exception:
            pass
    found = False
    browser.switch_to.window(browser.window_handles[-1])
    while (found == False):
        try:
            browser.find_element(By.ID, "download").click()
            found = True
        except Exception:
            pass
    found = False
    browser.switch_to.window(browser.window_handles[-1])
    while (found == False):
        try:
            links = browser.find_elements(By.CLASS_NAME, "mirror_link")[0]
            highest_qual = links.find_elements(By.CLASS_NAME, "dowload")[-1]
            epList.write(fileNameFormat % (epNum, formatString(highest_qual.text)) + "\n")
            epList.write(highest_qual.find_element(By.TAG_NAME, "a").get_attribute('href') + "\n")
            found = True
        except Exception:
            pass
    found = False
    browser.execute_script("window.close('');")
    browser.switch_to.window(browser.window_handles[-1])
    time.sleep(0.5)
    browser.execute_script("window.close('');")
    browser.switch_to.window(browser.window_handles[-1])
    browser.execute_script("clickOutsideEpisode();")
    epNum -= 1
browser.quit()