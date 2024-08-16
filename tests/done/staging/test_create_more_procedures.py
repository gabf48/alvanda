import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from pages.procedure_page import ProcedurePage

from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.mark.repeat(1)

def test_create_more_procedures(browser):
    login_page = LoginPage(browser)
    nav_bar = NavBar(browser)
    procedure_page = ProcedurePage(browser)

    login_page.login('gabriel.filip+nnn@wesrom.com', 'Parola1993!')
    time.sleep(10)

    nav_bar.pressBuilder()
    time.sleep(5)

    for _ in range(2):
        procedure_page.create_procedure()

    browser.quit()
