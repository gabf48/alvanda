import time

from selenium.webdriver.common.by import By
from utils.generate_random import GenerateRandom


class RoadMapPage:
    def __init__(self, driver):
        self.driver = driver

    def complete_action_step(self, x1, x2):
        generate_random = GenerateRandom(self.driver)
        random_string = generate_random.generate_random_string()
        for i in range(x1):
            if i == x2:
                break
            self.driver.find_element(By.CSS_SELECTOR, 'table > tbody > tr:nth-child(' + str(i) +') > td:nth-child(2) > div > textarea').click()
            self.driver.find_element(By.CSS_SELECTOR, 'table > tbody > tr:nth-child(' + str(i) +') > td:nth-child(2) > div > textarea').send_keys(random_string)
            time.sleep(5)
