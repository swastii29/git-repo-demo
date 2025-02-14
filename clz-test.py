from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Edge()
jobs=["BCA", "BIT","BBM","BscCsit"]

    browser.get('https://www.collegesnepal.com/')

    SearchBar = browser.find_element(By.ID, 'nav-head')

    SearchBar.send_keys(college)
    SearchBar.submit()
    time.sleep(1)
    print(college)

time.sleep(2)




browser.quit()