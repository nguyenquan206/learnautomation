from selenium import webdriver
from pages.home_page import HomePage
import time

from pages.login_page import LoginPage


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")

    homepage = HomePage(driver)
    homepage.click_form_auth()

    loginpage = LoginPage(driver)
    loginpage.input_username("tomsmith")
    loginpage.input_password("SuperSecretPassword!")
    loginpage.click_login()

    assert loginpage.is_logout_displayed()

    driver.quit()
