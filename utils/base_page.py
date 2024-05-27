from selenium.webdriver.common.by import By
import random

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def select_random_element_from_specific_list(self, list_selector):
        # Find a list of web elements
        element_list = self.driver.find_elements(By.CSS_SELECTOR, list_selector)

        # Select a random element from the list
        random_element = random.choice(element_list)

        # Perform actions with the selected element
        random_element.click()

    def select_random_element_from_specific_list(self, open_dropdown, list_selector):
        # open dropdown
        open_dropdown = self.driver.find_element(By.CSS_SELECTOR, open_dropdown).click()

        # Find a list of web elements
        element_list = self.driver.find_elements(By.CSS_SELECTOR, list_selector)

        # Select a random element from the list
        random_element = random.choice(element_list)

        # Perform actions with the selected element
        random_element.click()