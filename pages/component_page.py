import time
from selenium.webdriver.common.by import By

from utils.base_page import BasePage
from utils.generate_random import GenerateRandom

NEW_COMPONENT_BUTTON = '#react-tabs-3 button > div > div.Button_titleContainer__7vVZt'
COMPONENT_NAME = '[placeholder="Type here..."]'
COMPONENT_ICON_DROPDOWN = '[id="componentIcon"] [aria-label="toggle menu"]'
SAVE_AND_CONTINUE_BUTTON = '[src="/static/media/rightArrow.0bf8736fac13ad5e760635de92711332.svg"]'

TEXT_COMPONENT_ELEMENTS = '[data-tip="Text"]'

class ComponentPage:
    def __init__(self, driver):
        self.driver = driver

    def type_random_component_name(self):
        generate_random = GenerateRandom(self.driver)
        random_string = generate_random.generate_random_string()
        self.driver.find_element(By.CSS_SELECTOR, COMPONENT_NAME).send_keys(random_string)

    def select_random_component_icon(self):
        base_page = BasePage(self.driver)
        time.sleep(2)
        component_icon = self.driver.find_element(By.CSS_SELECTOR, COMPONENT_ICON_DROPDOWN).click()
        time.sleep(2)
        base_page.select_random_element_from_specific_list("#componentIcon img")

    def type_random_name_for_component_elements(self):
        generate_random = GenerateRandom(self.driver)
        random_string = generate_random.generate_random_string()
        self.driver.find_element(By.CSS_SELECTOR, '[type="input"]').send_keys(random_string)

    def select_random_component_elements(self):
        base_page = BasePage(self.driver)
        base_page.select_random_element_from_specific_list("#componentFields img")
        self.type_random_name_for_component_elements()

    def press_save_and_continue_button(self):
        self.driver.find_element(By.CSS_SELECTOR,SAVE_AND_CONTINUE_BUTTON).click()

    def select_text(self):
        self.driver.find_element(By.CSS_SELECTOR, TEXT_COMPONENT_ELEMENTS).click()
        self.type_random_name_for_component_elements()

    def create_component(self):
        self.driver.find_element(By.CSS_SELECTOR, NEW_COMPONENT_BUTTON).click()
        time.sleep(2)
        self.type_random_component_name()
        time.sleep(2)
        self.select_random_component_icon()
        self.select_text()
        self.press_save_and_continue_button()

    def check_name_component_list(self, expected_list):
        # Find all elements matching the CSS selector
        elements = self.driver.find_elements(By.CSS_SELECTOR,'#blueprint-card > div > div.blueprint-card-top-container > p')

        # Extract text from each element and store it in a list
        text_list = []
        for element in elements:
            text_list.append(element.text)

        # Print the list of text
        print(text_list)

        assert text_list == expected_list, "Text list does not match the expected list"
