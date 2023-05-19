import time

from selenium import webdriver
from pages.login_page import LoginPage



def test_workflow():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)

    #access Alvanda
    driver.get('https://front-end-dev.alvanda.com/')
    driver.maximize_window()

    #assert links for Terms and Conditions and Privacy and Policy
    login_page.check_links_for_terms_and_privacy()

    #assert link for Recover password page
    login_page.press_recover_password_button()
    current_url = driver.current_url
    assert current_url == 'https://front-end-dev.alvanda.com/reset-password'

    #login
    login_page.login('gabriel.filip@wesrom.com','Parola1993!')
    time.sleep(5)
