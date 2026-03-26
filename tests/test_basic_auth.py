from selenium import webdriver
from pages.home_page import HomePage
from pages.basic_auth_page import BasicAuthPage
import pyautogui

def test_basic_auth_successful():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")

    homepage = HomePage(driver)
    homepage.click_basic_auth()

    pyautogui.write("admin")
    pyautogui.press("tab")
    pyautogui.write("admin")
    pyautogui.press("enter")

    basic_auth = BasicAuthPage(driver)
    assert basic_auth.is_logging_successful()

def test_basic_auth_fail():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")

    homepage = HomePage(driver)
    homepage.click_basic_auth()

    pyautogui.press("esc")

    basic_auth = BasicAuthPage(driver)
    assert basic_auth.is_logging_fail()


