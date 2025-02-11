from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()

jobList = ["QA", "PHP", "Java"]

for job in jobList:
    browser.get('https://merojob.com')
    searchBar = browser.find_element(By.ID, 'job_search')
    searchBar.send_keys(job)
    searchBar.submit()
    time.sleep(5)

time.sleep(5)
browser.quit()