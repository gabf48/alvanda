import time

from selenium.webdriver.common.by import By

from utils.generate_random import GenerateRandom


class ProcedurePage:
    def __init__(self, driver):
        self.driver = driver

    def create_procedure(self):
        generate_random = GenerateRandom(self.driver)
        random_string = generate_random.generate_random_string()
        self.driver.find_element(By.CSS_SELECTOR,'.ProcessesPanel_controlsContainer__mZ2oH .Button_titleContainer__7vVZt > p').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,'[name="element-name"]').send_keys(random_string)
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,'body > reach-portal > div:nth-child(2) > div > div > div > div > div.ProcedureModal_controls__KvA4g > button > div > div.Button_titleContainer__7vVZt > p').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,'#root > div > main > div:nth-child(1) > div > div.ProcessInfo_procedureBuilderNameContainer__501X1 > button > div > div.Button_titleContainer__7vVZt > p').click()
        time.sleep(2)