#if i wanted an automation that fills out a form and submit it
#this how

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#contains keyboard keys eg shift, return ctrl etc
from selenium.webdriver.common.keys import Keys





# r prefix to the string indicates a raw string
#os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get("https://www.seleniumeasy.com/")
driver.implicitly_wait(5)

#handle popups
try:
    cancel_btn = driver.find_element(By.CLASS_NAME, 'cancel-button')
    cancel_btn.click()
except:
    print('No element found. skipiing...')

my_element = driver.find_element(By.ID, 'edit-search-block-form--2')

#make sure the input field is empty
my_element.clear()
my_element.send_keys("katalon")

#you could do this
    #submit = driver.find_element(By.CLASS_NAME, 'btn-primary')
    #submit.click()
#or this. its basically like pressing enter after typing
my_element.send_keys(Keys.RETURN)

time.sleep(30)
