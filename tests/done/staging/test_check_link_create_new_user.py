import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_check_link_create_new_user(browser):
    # Open the webpage
    browser.get("https://dev-web.alvanda.com/start-free-trial-step-1/")

    # Check if the text is present on the screen
    text_to_check = "503 Service Temporarily Unavailable"
    assert text_to_check not in browser.page_source, f"Test failed: '{text_to_check}' found on the screen"