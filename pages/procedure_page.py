import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.generate_random import GenerateRandom

class ProcedurePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # WebDriverWait with a timeout of 10 seconds

    def create_procedure(self):
        generate_random = GenerateRandom(self.driver)
        random_string = generate_random.generate_random_string()

        # Click the button to create a new procedure
        create_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ProcessesPanel_controlsContainer__mZ2oH .Button_titleContainer__7vVZt > p')))
        create_button.click()

        # Enter the random string into the input field
        input_field = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[name="element-name"]')))
        input_field.send_keys(random_string)

        # Click the button to confirm creating the procedure
        confirm_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > reach-portal > div:nth-child(2) > div > div > div > div > div.ProcedureModal_controls__KvA4g > button > div > div.Button_titleContainer__7vVZt > p')))
        confirm_button.click()

        # Click the button to save the procedure
        save_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > main > div:nth-child(1) > div > div.ProcessInfo_procedureBuilderNameContainer__501X1 > button > div > div.Button_titleContainer__7vVZt > p')))
        save_button.click()
