import booking.constants as const
import os
from selenium.webdriver.common.by import By
from selenium import webdriver

class Booking(webdriver.Chrome):
    #constructor
    def __init__(self, driver_path=r"C:/SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        #instantiate an instance of webdriver
        super(Booking, self).__init__()
        self.implicitly_wait(10)
        self.maximize_window()


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()


    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()
        selected_currency = self.find_element(
            By.CSS_SELECTOR, 
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency.click()

    def select_place_to_go(self, place_to_go):
        search_element = self.find_element(By.ID, 'ss')
        search_element.clear()
        search_element.send_keys(place_to_go)

        first_result = self.find_element(
            By.CSS_SELECTOR, 
            'li[data-i="0"]'
        )
        first_result.click()


    def select_dates(self, check_in, check_out):
        check_in_element = self.find_element(
            By.CSS_SELECTOR, 
            f'td[data-date="{check_in}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR, 
            f'td[data-date="{check_out}"]'
        )
        check_out_element.click()

    def select_adults(self, count=1):
        select_adults_element = self.find_element(By.ID, 'xp__guests__toggle')
        select_adults_element.click()

        while True:
            #make sure count is minmum
            decrease_adults_element = self.find_element(
                By.CSS_SELECTOR, 
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()
            #if count is 1 "bare min" get out of the loop
            adults_cur_value = self.find_element(
                By.ID, 
                'group_adults'
            )
            # lets get the value of the count
            count_value = adults_cur_value.get_attribute('value')

            # we type cast it to an int since it is initially a string
            if int(count_value) == 1:
                break

        increase_adults_element = self.find_element(
            By.CSS_SELECTOR, 
            'button[aria-label="Increase number of Adults"]'
        )

        #click click click
        for _ in range(count - 1):
            increase_adults_element.click()