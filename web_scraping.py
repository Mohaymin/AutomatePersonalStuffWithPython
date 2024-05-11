from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# web_base_url = "https://www.fortishealthcare.com/doctors/location/kolkata"
web_base_url = "https://stackoverflow.com/questions/tagged/android"

driver = webdriver.Chrome()
driver.get(web_base_url)
time.sleep(5)

question_titles = driver.find_elements(By.CLASS_NAME, "s-post-summary--content-title")
for question in question_titles:
    print(question.text)





