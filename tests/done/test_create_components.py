import time
import pytest
from selenium import webdriver
from pages.builder_page import BuilderPage
from pages.component_page import ComponentPage
from pages.login_page import LoginPage
from pages.nav_bar import NavBar

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver

def test_create_components(browser):
    login_page = LoginPage(browser)
    nav_bar = NavBar(browser)
    builder_page = BuilderPage(browser)
    component_page = ComponentPage(browser)

    login_page.login('gabriel.filip+122fsadkfj3ioas23@wesrom.com', 'Parola1993!')
    time.sleep(5)

    nav_bar.pressBuilder()
    time.sleep(2)

    builder_page.selectComponentSection()
    time.sleep(2)

    for _ in range(5):
        component_page.create_component()

    time.sleep(10)
