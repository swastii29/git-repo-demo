from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get('https://bing.com')

time.sleep(5)

element = driver.find_element(By.ID, 'sb_form_q')
element.send_keys('Quantum Infosys Pvt. Ltd Biratnagar')
element.submit()

time.sleep(5)
driver.quit()