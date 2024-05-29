from selenium.webdriver.common.by import By

from utils import generate_random
from utils.base_page import BasePage
from utils.generate_random import GenerateRandom

NEW_TASK_BUTTON = 'div:nth-child(3) > button:nth-child(2) > div'
TASK_NAME_INPUT = 'div:nth-child(1) > div.StyledInput_inputHostContainer__sHK8F > input'
ASSIGNEE_DROPDOWN = 'div.TaskForm_assigneeCreatorContainer__0c5V7 > div > div button'
PROCEDURE_DROPDOWN = 'form div:nth-child(4) button svg'
CREATE_AND_START_BUTTON = 'body > reach-portal > div:nth-child(2) button:nth-child(2) > div > div.Button_titleContainer__7vVZt'
EMAIL_INPUT = '[name="email"]'
NUMBER_INPUT = '[inputmode="numeric"]'
TEXT_INPUT = '[name="text"]'
class TaskPage:

    def __init__(self, driver):
        self.driver = driver

    def press_create_new_task(self):
        self.driver.find_element(By.CSS_SELECTOR, NEW_TASK_BUTTON).click()

    def select_specific_task_responsible(self, responsible):
        base_page = BasePage(self.driver)
        base_page.select_specific_element_from_list(ASSIGNEE_DROPDOWN, 'div > ul > li > span > div', responsible)

    def select_specific_procedure(self, procedure):
        base_page = BasePage(self.driver)
        base_page.select_specific_element_from_list(PROCEDURE_DROPDOWN, 'div > ul > li > span > div', procedure)

    def complete_task_modal_specific_responsible_and_procedure(self, responsible, procedure):
        base_page = BasePage(self.driver)
        generate_random = GenerateRandom(self.driver)
        random_string = generate_random.generate_random_string()
        self.driver.find_element(By.CSS_SELECTOR, TASK_NAME_INPUT).send_keys(random_string)
        self.select_specific_task_responsible(responsible)
        self.select_specific_procedure(procedure)
        self.press_create_and_start_button()

    def select_random_procedure(self):
        base_page = BasePage(self.driver)
        base_page.select_random_element_from_specific_list('div.SelectComponents_toggleBtnChildren__29RMx.TaskForm_toggleBtnChildren__ccjp\+ > p','div > ul > li > span > div')

    def press_create_and_start_button(self):
        self.driver.find_element(By.CSS_SELECTOR, CREATE_AND_START_BUTTON).click()

    def type_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, EMAIL_INPUT).send_keys(email)

    def type_number(self, number):
        self.driver.find_element(By.CSS_SELECTOR, NUMBER_INPUT).send_keys(number)

    def type_text(self, text):
        self.driver.find_element(By.CSS_SELECTOR, TEXT_INPUT).send_keys(text)
