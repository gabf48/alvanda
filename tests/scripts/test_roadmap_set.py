import time
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from pages.procedure_page import ProcedurePage
from pages.roadmap_page import RoadMapPage


from selenium.webdriver.chrome.options import Options
@pytest.fixture(scope="function")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.mark.repeat(1)

def test_roadmap_set(browser):
    login_page = LoginPage(browser)
    roadmap_page = RoadMapPage(browser)

    login_page.login('gabriel.filip+master@wesrom.com', 'Parola1993!')

    browser.get("https://front-end-dev.alvanda.com/strategic-roadmap/initiative?id=9af71fc7-4573-4690-b4c1-ce815a48d323")
    time.sleep(15)
    roadmap_page.complete_action_step(3,10)
    time.sleep(2000)