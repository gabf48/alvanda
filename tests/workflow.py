import time

from selenium import webdriver
from pages.login_page import LoginPage



def test_workflow():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)


    login_page.login('gabriel.filip@wesrom.com','Parola1993!')
    time.sleep(10)
