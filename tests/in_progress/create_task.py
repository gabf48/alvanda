import time
import pytest
from selenium import webdriver
from pages.builder_page import BuilderPage
from pages.component_page import ComponentPage
from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from pages.task_page import TaskPage
from utils.generate_random import GenerateRandom


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver

def test_create_task(browser):
    login_page = LoginPage(browser)
    nav_bar = NavBar(browser)
    builder_page = BuilderPage(browser)
    component_page = ComponentPage(browser)
    task_page = TaskPage(browser)
    generate_random = GenerateRandom(browser)


    login_page.login('gabriel.filip+master@wesrom.com', 'Parola1993!')

    nav_bar.pressTasks()
    time.sleep(2)
    task_page.press_create_new_task()
    time.sleep(2)
    task_page.complete_task_modal_specific_responsible_and_procedure("Gabriel Admin","Correct procedure")
    time.sleep(10)
    task_page.type_email("test@test.com")
    task_page.type_number("100")
    task_page.type_text(generate_random.generate_random_string())
    task_page.press_complete_task_button()
    time.sleep(10)
    task_page.check_modal_text()
    time.sleep(5000000)
