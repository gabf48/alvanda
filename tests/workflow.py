import time

from selenium import webdriver

from pages.builder_page import BuilderPage
from pages.component_page import ComponentPage
from pages.login_page import LoginPage
from pages.nav_bar import NavBar


def test_workflow():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    nav_bar = NavBar(driver)
    builder_page = BuilderPage(driver)
    component_page = ComponentPage(driver)

    #access Alvanda
    # driver.get('https://front-end-dev.alvanda.com/')
    # driver.maximize_window()
    #
    # #assert links for Terms and Conditions and Privacy and Policy
    # login_page.check_links_for_terms_and_privacy()
    #
    # #assert link for Recover password page
    # login_page.press_recover_password_button()
    # current_url = driver.current_url
    # assert current_url == 'https://front-end-dev.alvanda.com/reset-password'

    #login
    login_page.login('gabriel.filip+122fsadkfj3ioas23@wesrom.com','Parola1993!')
    time.sleep(5)

    #open builder
    nav_bar.pressBuilder()
    time.sleep(2)

    #open component section
    builder_page.selectComponentSection()
    time.sleep(2)

    #create component
    for _ in range(50):
        component_page.create_component()

    time.sleep(10)
