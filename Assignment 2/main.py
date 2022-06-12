import time
from selenium import webdriver
import requests
import json
import random

# Constants
PATH = './chromedriver.exe'
DETAILS_API = 'https://api.namefake.com/'
TARGET = 'https://docs.google.com/forms/d/e/1FAIpQLSdlHVzoMEoolhoUjsH9h2D1kIqA2-AYpVb0P959Uq48uLNxOw/viewform?usp=sf_link'
# Load driver
driver = webdriver.Chrome(PATH)
# Get user details
request = requests.get(DETAILS_API)
user_data = json.loads(request.text)
# Open Chrome and wait for page loading to complete
driver.get(TARGET)
time.sleep(3)

"""Find elements with xpath and add data to them """
# Name
name_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input') 
name_field.send_keys(user_data.get('name'))
time.sleep(2)
# Address
address_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
address_field.send_keys(user_data.get('address')) # Write name from user_data in the field
time.sleep(2)
# Gender 
gender = user_data.get("pict")[1:]
if gender == "male":
    gender_xpath = '//*[@id="i13"]/div[3]/div'
elif gender == 'female':
    gender_xpath = '//*[@id="i16"]/div[3]/div'
else:
    gender_xpath = '//*[@id="i19"]/div[3]/div'

gender_option = driver.find_element_by_xpath(gender_xpath)
gender_option.click()
time.sleep(2)
# Email
email_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
email_field.send_keys(user_data.get('email_u') + '@mail.com')
time.sleep(2)
# Status
status_choice = random.choice([0, 1])
if status_choice == 1:
    status_xpath = '//*[@id="i30"]/div[3]/div'
else:
    status_xpath = '//*[@id="i33"]/div[3]/div'

status_choice = driver.find_element_by_xpath(status_xpath)
status_choice.click()
time.sleep(2)
# Submit
submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit_button.click()
time.sleep(5)

driver.quit()