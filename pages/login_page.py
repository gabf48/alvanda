import time

from selenium.webdriver.common.by import By

EMAIL_INPUT = '[name="email"]'
PASSWORD_INPUT = '[name="password"]'
BUTTON_SIGN_IN = '[type="submit"]'
BUTTON_CONTINUE = '[role="dialog"] div:nth-child(2) [comp-state="enabled"]'


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.maximize_window()
        self.driver.get('https://front-end-dev.alvanda.com/')
        time.sleep(5)
        type_email = self.driver.find_element(By.CSS_SELECTOR, EMAIL_INPUT).send_keys(email)
        type_password = self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(password)
        press_sign_in_button = self.driver.find_element(By.CSS_SELECTOR, BUTTON_SIGN_IN).click()
        time.sleep(5)
        try:
            self.driver.find_element(By.CSS_SELECTOR, BUTTON_CONTINUE).click()
        except Exception as e:
            print(f"Upgrade modal don't displayed: {e}")

    def check_links_for_terms_and_privacy(self):
        x = self.driver.find_element(By.CSS_SELECTOR,
                                     'div.Login_firstContainerContent__wbbdK > form > p > a:nth-child(1)').get_attribute(
            'href')
        print(x)
        y = self.driver.find_element(By.CSS_SELECTOR,
                                     'div.Login_firstContainerContent__wbbdK > form > p > a:nth-child(2)').get_attribute(
            'href')
        print(y)

        assert x == 'https://alvanda.com/terms-conditions'
        assert y == 'https://alvanda.com/privacy-policy'

    def press_recover_password_button(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 'div.Login_firstContainerContent__wbbdK > div > button > div > div > p').click()
