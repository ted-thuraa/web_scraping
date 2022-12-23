#contains class with instance methods 
#responsible for applying filtrations
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    #to our bot receive more than one star rating we use *star_value
    #its simply turning it into an arbitrary argument
    def apply_star_rating(self, *star_values):
        #get section box
        star_filtration_box = self.driver.find_element(
            By.CSS_SELECTOR, 
            'div[data-filters-group="class"]'
        )
        #gets box all child elements
        star_child_elements = star_filtration_box.find_elements(
            By.CSS_SELECTOR, 
            '*'
        )
       
        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()

    def sort_price_lowest_first(self):
        sort_drop_down = self.driver.find_element(
            By.CSS_SELECTOR, 
            'button[data-testid="sorters-dropdown-trigger"]'
        )
        sort_drop_down.click()


        sort_from_lowest = self.driver.find_element(
            By.CSS_SELECTOR, 
            'button[data-id="price"]'
        )
        sort_from_lowest.click()