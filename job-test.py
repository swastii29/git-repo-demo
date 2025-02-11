from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()
jobs = ["QA", "SEO", "Graphic designer"]

for job in jobs:
    print(job)
    browser.get('https://merojob.com')
    searchBar = browser.find_element(By.ID, 'job_search')
    searchBar.send_keys(job)
    searchBar.submit()
    time.sleep(5)   

time.sleep(5)
'''
job_items=driver.find_elements(By.CLASS_Name,"job-item")
print(f"job search results for '{find_job}':\n")
for job in job_items:
    if job.is_displayed():
        print(job.text)
        print("find a job for it student")
'''
browser.quit()
