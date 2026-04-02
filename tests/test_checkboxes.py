import time

from selenium import webdriver
from pages.home_page import HomePage
from pages.checkboxes_page import Checkboxes

def test_checkboxes_page(driver):
    driver.get("https://the-internet.herokuapp.com/")

    homepage = HomePage(driver)
    homepage.click_checkboxes()

    checkboxes = Checkboxes(driver)
    #Verify default value
    assert not checkboxes.is_checked_by_index(0)
    assert checkboxes.is_checked_by_index(1)

    #Tick checkbox and verify
    checkboxes.tick_checkboxes_by_index(0)
    assert checkboxes.is_checked_by_index(0)
    time.sleep(5)

    #Untick checkbox and verify
    checkboxes.untick_checkboxes_by_index(1)
    assert not checkboxes.is_checked_by_index(1)
    time.sleep(5)