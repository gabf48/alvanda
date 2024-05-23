import time
import pytest
from selenium import webdriver
from pages.builder_page import BuilderPage
from pages.component_page import ComponentPage
from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from utils.lists import by_default_component_name_list

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver

def test_check_by_default_components(browser):
    # Setup and actions
    browser.maximize_window()
    login_page = LoginPage(browser)
    login_page.login('gabriel.filip+defaultComponent@wesrom.com', 'Parola1993!')

    time.sleep(5)

    nav_bar = NavBar(browser)
    nav_bar.pressBuilder()
    time.sleep(2)

    builder_page = BuilderPage(browser)
    builder_page.selectComponentSection()
    time.sleep(5)

    component_page = ComponentPage(browser)
    component_page.check_name_component_list(by_default_component_name_list)
    time.sleep(2)

    # Assertions
    assert browser.title == "Alvanda"
    assert "Alvanda" in browser.title

