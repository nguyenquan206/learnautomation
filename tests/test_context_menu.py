from selenium import webdriver
from pages.home_page import HomePage
from pages.context_menu_page import ContextMenuPage

def test_context_menu():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/")

    homepage = HomePage(driver)
    homepage.click_context_menu()

    contextmenu = ContextMenuPage(driver)
    contextmenu.right_click_context_menu()
    alert = driver.switch_to.alert
    assert "You selected a context menu" in alert.text
    alert.accept()