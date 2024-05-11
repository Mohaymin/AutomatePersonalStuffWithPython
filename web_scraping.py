from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

file_name = 'doctor_names.csv'
doctor_count = 0

with open(file_name, 'w') as file:
    file.write('name; speciality \n')

    # web_base_url = "https://www.fortishealthcare.com/doctors/location/kolkata"
    for page in range(13):
        web_base_url = f"https://www.fortishealthcare.com/doctors/location/kolkata?field_hospitals=3516&field_speciality=All&location%5B297%5D=297&location%5B465%5D=465&sub_specialities=All&search_api_fulltext=&page={page}"

        driver = webdriver.Chrome()
        driver.get(web_base_url)
        # time.sleep(3)

        # Wait for the element to be clickable before proceeding (optional)
        try:
            wait = WebDriverWait(driver, 10)  # Set a 10-second wait timeout
            hospital_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "edit-field-hospitals")))
            pager_element = wait.until(EC.presence_of_element_located((By.XPATH, """//*[@id="block-fortis-content"]/div/div/div""")))
        except:
            print("Hospital dropdown element not found or not clickable within 10 seconds.")
            driver.quit()
            exit(1)

        # Now use the Select class on the single element
        select_hospital = Select(hospital_dropdown)
        select_hospital.select_by_value('3516')

        time.sleep(3)  # Optional pause to see the selection

        doctor_names = driver.find_elements(By.CLASS_NAME, "doctor_name")
        doctor_specialities = driver.find_elements(By.CLASS_NAME, "doctor_specialities")

        for name, speciality in zip(doctor_names, doctor_specialities):
            print(f"{name.text} : {speciality.text}")
            doctor_count = doctor_count + 1
            file.write(f"{name.text}; {speciality.text} \n")
            
        print(f"Print count: {doctor_count}")
        driver.quit()

print(f"Total Doctors: {doctor_count}")



