from selenium.webdriver.common.by import By

EMAIL_INPUT = '[name="email"]'
PASSWORD_INPUT = '[name="password"]'
BUTTON_SIGN_IN = '[type="submit"]'
class LoginPage:

    def __init__(self, driver):
        self.driver = driver
    def login(self,email,password):
        self.driver.maximize_window()
        self.driver.get('https://front-end-dev.alvanda.com/')
        type_email = self.driver.find_element(By.CSS_SELECTOR,EMAIL_INPUT).send_keys(email)
        type_password = self.driver.find_element(By.CSS_SELECTOR,PASSWORD_INPUT).send_keys(password)
        press_sign_in_button = self.driver.find_element(By.CSS_SELECTOR, BUTTON_SIGN_IN).click()