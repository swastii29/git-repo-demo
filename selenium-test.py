from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
collegeList = ["top college in biratnagar","top college in kathmandu","top college in Dharan"]
myString = ""

for college in collegeList:
    print(college)
    browser.get('https://bing.com')
    searchBar = browser.find_element(By.ID, 'sb_form_q')
    searchBar.send_keys('Colleges in Nepal')
    searchBar.submit()
    links = browser . find_element(By.TAG_NAME, 'h1')

time.sleep(3)
print(myString)
file = open('test.txt', 'w')
file.write(myString)
file.close()

time.sleep(5)
browser.quit()