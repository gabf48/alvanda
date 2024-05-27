import time

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

    def select_specific_element_from_list(self, open_dropdown, list_selector, item_text):
        # Open the dropdown
        self.driver.find_element(By.CSS_SELECTOR, open_dropdown).click()

        # Find a list of web elements
        element_list = self.driver.find_elements(By.CSS_SELECTOR, list_selector)

        # Filter the list to find the element that matches the item_text
        matching_element = None
        for element in element_list:
            if element.text == item_text:
                matching_element = element
                break

        # Check if the matching element is found
        if matching_element:
            # Perform actions with the selected element
            matching_element.click()
        else:
            raise ValueError(f"No element with text '{item_text}' found in the list.")