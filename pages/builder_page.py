from selenium.webdriver.common.by import By

COMPONENT_SECTION = '#react-tabs-2'
class BuilderPage:
    def __init__(self, driver):
        self.driver = driver

    def selectComponentSection(self):
        component_section_button = self.driver.find_element(By.CSS_SELECTOR, COMPONENT_SECTION).click()
