from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Edge()
jobs=["QA", "PHP","Java"]
for job in jobs:
    browser.get('https://merojob.com')

    SearchBar = browser.find_element(By.ID, 'job_search')

    SearchBar.send_keys(job)
    SearchBar.submit()
    time.sleep(1)
    print(job)

time.sleep(2)




browser.quit()