import time
from selenium import webdriver
from pages.builder_page import BuilderPage
from pages.component_page import ComponentPage
from pages.login_page import LoginPage
from pages.nav_bar import NavBar

def test_create_components():
    driver = webdriver.Chrome(
        executable_path='D:/alvanda/browsers/chromedriver.exe')
    login_page = LoginPage(driver)
    nav_bar = NavBar(driver)
    builder_page = BuilderPage(driver)
    component_page = ComponentPage(driver)

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
    for _ in range(10):
        component_page.create_component()

    time.sleep(10)
