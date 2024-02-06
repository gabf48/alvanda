import time
from selenium import webdriver
from pages.builder_page import BuilderPage
from pages.component_page import ComponentPage
from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from utils.lists import by_default_component_name_list

driver = webdriver.Chrome()
login_page = LoginPage(driver)
nav_bar = NavBar(driver)
builder_page = BuilderPage(driver)
component_page = ComponentPage(driver)

# login
login_page.login('gabriel.filip+autoTest@wesrom.com','Parola1993!')
time.sleep(5)

# open builder
nav_bar.pressBuilder()
time.sleep(2)

# open component section
builder_page.selectComponentSection()
time.sleep(5)
component_page.check_name_component_list(by_default_component_name_list)
time.sleep(2)
