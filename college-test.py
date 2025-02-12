from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
courses = ["BIM", "BCA", "BscCsit"]

for course in courses:
    print(course)
    browser.get('https://edusanjal.com/')
    searchBar = browser.find_element(By.ID, 'Courses_search')
    searchBar.send_keys()
    searchBar.submit()
    time.sleep(5)   

time.sleep(5)

browser.quit()