from selenium.webdriver.common.by import By

from utils.base_page import BasePage

NEW_TASK_BUTTON = 'div:nth-child(3) > button:nth-child(2) > div'
TASK_NAME_INPUT = 'div:nth-child(1) > div.StyledInput_inputHostContainer__sHK8F > input'
class TaskPage:

    def __init__(self, driver):
        self.driver = driver

    def press_create_new_task(self):
        self.driver.find_element(By.CSS_SELECTOR, NEW_TASK_BUTTON).click()

    def complete_task_modal(self, task_name):
        base_page = BasePage(self.driver)
        self.driver.find_element(By.CSS_SELECTOR, TASK_NAME_INPUT).send_keys(task_name)
        base_page.select_random_element_from_specific_list()