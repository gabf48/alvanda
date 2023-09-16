import time
from selenium import webdriver
from pages.builder_page import BuilderPage
from pages.component_page import ComponentPage
from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from pages.procedure_page import ProcedurePage


def test_create_procedures():
    driver = webdriver.Chrome(
        executable_path='C:/projects python/browsers/chromedriver.exe')
    login_page = LoginPage(driver)
    nav_bar = NavBar(driver)
    builder_page = BuilderPage(driver)
    component_page = ComponentPage(driver)
    procedure_page = ProcedurePage(driver)

    #login
    login_page.login('gabriel.filip+122fsadkfj3ioas23@wesrom.com','Parola1993!')

    #go procedures page
    nav_bar.pressBuilder()

    #create_procedures
    time.sleep(5)
    for _ in range(40):
        procedure_page.create_procedure()
