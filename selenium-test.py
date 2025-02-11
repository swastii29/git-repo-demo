from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
browser.get('https://bing.com')

time.sleep(2)

SearchBar = browser.find_element(By.ID, 'sb_form_q')
SearchBar.send_keys('Mahendra Morang Campus Biratnagar')
SearchBar.submit()

time.sleep(5)
browser.quit()