from selenium import webdriver
from pages.home_page import HomePage
from pages.disappear_element_page import DisappearElementPage

def test_disappear_element_page():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")

    homepage = HomePage(driver)
    homepage.click_disappear_element()

    disappear_element = DisappearElementPage(driver)
    #Verify disappearing menu
    base_url = "https://the-internet.herokuapp.com/"
    disappear_element.verify_disappearing_menu(base_url)

