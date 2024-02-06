import time
from selenium import webdriver
from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from pages.procedure_page import ProcedurePage

driver = webdriver.Chrome()
login_page = LoginPage(driver)
nav_bar = NavBar(driver)
procedure_page = ProcedurePage(driver)

# login
login_page.login('gabriel.filip+master@wesrom.com', 'Parola1993!')

# go procedures page
time.sleep(10)
nav_bar.pressBuilder()

# create_procedures
time.sleep(5)
for _ in range(2):
    procedure_page.create_procedure()