import time
import pytest
from selenium import webdriver
from pages.builder_page import BuilderPage
from pages.component_page import ComponentPage
from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.mark.repeat(1)

def test_create_components(browser):
    login_page = LoginPage(browser)
    nav_bar = NavBar(browser)
    builder_page = BuilderPage(browser)
    component_page = ComponentPage(browser)

    login_page.login('gabriel.filip+nnn@wesrom.com', 'Parola1993!')
    time.sleep(5)

    nav_bar.pressBuilder()
    time.sleep(2)

    builder_page.selectComponentSection()
    time.sleep(2)

    for _ in range(5):
        component_page.create_component()

