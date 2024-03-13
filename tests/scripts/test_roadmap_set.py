import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from pages.procedure_page import ProcedurePage
from pages.roadmap_page import RoadMapPage


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver

def test_roadmap_set(browser):
    login_page = LoginPage(browser)
    roadmap_page = RoadMapPage(browser)

    login_page.login('gabriel.filip+master@wesrom.com', 'Parola1993!')

    browser.get("https://front-end-dev.alvanda.com/strategic-roadmap/initiative?id=9af71fc7-4573-4690-b4c1-ce815a48d323")
    time.sleep(15)
    roadmap_page.complete_action_step(3,10)
    time.sleep(2000)