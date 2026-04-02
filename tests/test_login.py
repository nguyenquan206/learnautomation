from selenium import webdriver
from pages.home_page import HomePage
import time

from pages.login_page import LoginPage


def test_login_successfully(driver):
    driver.get("https://the-internet.herokuapp.com/")

    homepage = HomePage(driver)
    homepage.click_form_auth()

    loginpage = LoginPage(driver)
    loginpage.input_username("tomsmith")
    loginpage.input_password("SuperSecretPassword!")
    loginpage.click_login()

    assert loginpage.is_logout_displayed()

    driver.quit()

def test_login_fail(driver):
    driver.get("https://the-internet.herokuapp.com/")
    homepage = HomePage(driver)
    homepage.click_form_auth()
    loginpage = LoginPage(driver)
    loginpage.input_username("wrongusername")
    loginpage.input_password("wrongpassword")
    loginpage.click_login()

    assert not loginpage.is_logout_displayed()
    assert loginpage.is_loggin_fail_text_displayed()

    driver.quit()
