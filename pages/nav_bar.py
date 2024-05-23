from selenium.webdriver.common.by import By

BUILDER_BUTTON = '[src="/static/media/blueprintsMenuIcon.287da4747f8d5335b0c41c7648a8305e.svg"]'
TASKS_BUTTON = '[href="/tasks"]'
class NavBar:

    def __init__(self, driver):
        self.driver = driver

    def pressBuilder(self):
        builder_icon = self.driver.find_element(By.CSS_SELECTOR,BUILDER_BUTTON).click()

    def pressTasks(self):
        self.driver.find_element(By.CSS_SELECTOR,TASKS_BUTTON).click()
