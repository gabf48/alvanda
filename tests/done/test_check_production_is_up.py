import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver

def test_check_production_is_up(browser):
    browser.get('https://alvanda.com/')

    # Find all elements with class "elementor-button-text"
    elements = browser.find_elements(By.CSS_SELECTOR,'[class="elementor-button-text"]')

    # Get the size of the list of elements
    size_of_list = len(elements)

    # Assert that the size of the list is equal to 5
    assert size_of_list == 5, f"The size of the list is not equal to 5. It is {size_of_list}."

    # If the assertion passes, this line will be executed
    print("The size of the list is equal to 5.")

