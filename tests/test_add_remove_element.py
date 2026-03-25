import random

from selenium import webdriver
from pages.home_page import HomePage
from pages.add_remove_element_page import AddRemoveElementPage

def test_add_remove_elements():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")

    home_page = HomePage(driver)
    home_page.click_add_remove_element()

    add_remove_element = AddRemoveElementPage(driver)
    times = random.randint(1, 10)
    add_remove_element.click_add_multiple_elements(times)
    assert add_remove_element.count_delete_element_button() == times

    add_remove_element.click_delete_multiple_elements(times)
    assert add_remove_element.count_delete_element_button() == 0
