import pytest
from selenium.webdriver import Chrome
from done.test_create_more_procedures import test_create_more_procedures
from done.test_create_components import test_create_components
from done.test_check_by_default_components import test_check_by_default_components
from done.test_check_production_is_up import test_check_production_is_up

@pytest.fixture(scope="module")
def browser():
    # Setup code to create the browser instance
    driver = Chrome()
    yield driver

def test_suite(browser):
    # Run the test function with the browser fixture
    test_create_more_procedures(browser)
    test_create_components(browser)
    test_check_by_default_components(browser)
    test_check_production_is_up(browser)
