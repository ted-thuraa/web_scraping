import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# r prefix to the string indicates a raw string
#os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get("https://www.seleniumeasy.com/")
driver.implicitly_wait(6)
my_element = driver.find_element(By.LINK_TEXT, 'TestNG')
my_element.click()
time.sleep(30)


# if i was automitating a download button that waits until it outputs somewhere
# "completed" when the download is complete
# this how you would implement it

#        WebDriverWait(driver, 30) . until(
#            #until we see completed the download is over
#            EC.text_to_be_present_in_element(
#                (By.CLASS_NAME, 'progress_label'),  # element filtration
#                'completed'     # expected text
#            )
#        )


